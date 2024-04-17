#include "SubPixelPostProcess.h"
#include "OpticalFlowUploader.h"

using namespace std;

struct DotWindows {
    uint32_t up{0};
    uint32_t down{0};
    uint32_t left{0};
    uint32_t center{0};
    uint32_t right{0};
};

__device__ DotWindows dot_windows(CudaImageRef<uint8_t> src_img, CudaImageRef<uint8_t> dst_img, PointU32 src_center, PointU32 dst_center, uint32_t window_size) {
    PointU32 top_left_offset{window_size / 2, window_size / 2};
    if (top_left_offset.x + 1 > src_center.x || top_left_offset.x + 1 > dst_center.x ||
        top_left_offset.y + 1 > src_center.y || top_left_offset.y + 1 > dst_center.y) {
        // would go negative outside of image bounds
        return {};
    }

    Point src_top_left = src_center - top_left_offset;
    Point dst_top_left = dst_center - top_left_offset;
    if (src_top_left.x + window_size + 1 > src_img.width || dst_top_left.x + window_size + 1 > dst_img.width ||
        src_top_left.y + window_size + 1 > src_img.height || dst_top_left.y + window_size + 1 > dst_img.height) {
        // would go greater than image bounds, invalid
        return {};
    }

    DotWindows sums;
    uint8_t* src_addr = src_img.get_addr(src_top_left);
    uint8_t* dst_addr = dst_img.get_addr(dst_top_left);
    for (uint32_t y_off = 0; y_off < window_size; y_off++) {
        uint32_t left = *(dst_addr - 1);
        uint32_t center = *dst_addr;
        uint32_t right = *(dst_addr + 1);
        for (uint32_t x_off = 0; x_off < window_size; x_off++) {
            uint32_t src_val = *src_addr;
            sums.up += src_val * *(dst_addr - dst_img.pitch);
            sums.down += src_val * *(dst_addr + dst_img.pitch);
            sums.left += src_val * left;
            sums.center += src_val * center;
            sums.right += src_val * right;

            src_addr += 1;
            dst_addr += 1;

            left = center;
            center = right;
            right = *(dst_addr + 1);
        }
        src_addr += src_img.pitch;
        dst_addr += dst_img.pitch;
    }

    return sums;
}

__global__
void refine(CudaImageRef<uint8_t> src_img,
            CudaImageRef<uint8_t> dst_img,
            CudaImageRef<S105Vector> vectors, uint32_t block_size,
            CudaImageRef<Point<float>> out_img, uint32_t window_size, uint32_t boundary_skip_size) {
    uint32_t x = blockIdx.x * blockDim.x + threadIdx.x + boundary_skip_size;
    uint32_t y = blockIdx.y * blockDim.y + threadIdx.y + boundary_skip_size;

    if (x < vectors.width && y < vectors.height) {
        PointU32 src_pt{x * block_size + (block_size - 1) / 2, y * block_size + (block_size - 1) / 2};
        auto vec_initial_guess_s105 = vectors.read({x, y});
        auto vec_initial_guess_rounded = s105_to_point_rounded(vec_initial_guess_s105);

        auto dst_pt_int = PointI32{static_cast<int32_t>(src_pt.x), static_cast<int32_t>(src_pt.y)} + vec_initial_guess_rounded;
        if (dst_pt_int.x <= 0 || dst_pt_int.y <= 0 || dst_pt_int.x >= (dst_img.width - 1) || dst_pt_int.y >= (dst_img.height - 1)) {
            // vector (+/- 1px) goes outside of destination image, don't do refinement
            out_img.write({x, y}, s105_to_point_float(vec_initial_guess_s105));
            return;
        }
        PointU32 dst_pt{static_cast<uint32_t>(dst_pt_int.x), static_cast<uint32_t>(dst_pt_int.y)};

        auto sums = dot_windows(src_img, dst_img, src_pt, dst_pt, window_size);

        if (sums.up == 0 || sums.down == 0 || sums.left == 0 || sums.right == 0 || sums.center == 0) {
            // invalid dot product, don't do refinement
            out_img.write({x, y}, s105_to_point_float(vec_initial_guess_s105));
        } else {
            // fit [left, center, right] to a gaussian distribution
            float x_mean = (logf((float) sums.left) - logf((float) sums.right)) / (2 * logf((float) sums.left) - 4 * logf((float) sums.center) + 2 * logf((float) sums.right));
            float y_mean = (logf((float) sums.up) - logf((float) sums.down)) / (2 * logf((float) sums.up) - 4 * logf((float) sums.center) + 2 * logf((float) sums.down));

            Point<float> refined = {static_cast<float>(vec_initial_guess_rounded.x) + x_mean,
                                    static_cast<float>(vec_initial_guess_rounded.y) + y_mean};
            out_img.write({x, y}, refined);
        }
    }
}

// copy the top and bottom border, including corners
__global__ void copy_border_top_bottom(CudaImageRef<S105Vector> vectors, CudaImageRef<Point<float>> out_img, uint32_t boundary_skip_size) {
    uint32_t x = blockIdx.x * blockDim.x + threadIdx.x;
    uint32_t y = blockIdx.y * blockDim.y + threadIdx.y;
    if (x >= out_img.width || y >= 2 * boundary_skip_size) {
        return;
    }
    if (y >= boundary_skip_size) {
        y = y - 2*boundary_skip_size + out_img.height;
    }
    out_img.write({x, y}, s105_to_point_float(vectors.read({x, y})));
}

// copy the left and right borders, excluding the corners
__global__ void copy_border_sides(CudaImageRef<S105Vector> vectors, CudaImageRef<Point<float>> out_img, uint32_t boundary_skip_size) {
    uint32_t x = blockIdx.x * blockDim.x + threadIdx.x;
    uint32_t y = blockIdx.y * blockDim.y + threadIdx.y;
    if (x >= 2 * boundary_skip_size || y >= out_img.height - 2 * boundary_skip_size) {
        return;
    }
    if (x >= boundary_skip_size) {
        x = x - 2*boundary_skip_size + out_img.width;
    }
    out_img.write({x, y}, s105_to_point_float(vectors.read({x, y})));
}

void SubPixelPostProcess::process_image(const std::shared_ptr<OpticalFlowImage> &img) {
    auto orig_vecs = img->GetGpuFlowVectorsRef();
    if (orig_vecs) {
        auto out = std::make_shared<CudaImageOwned<Point<float>>>(orig_vecs->width, orig_vecs->height);

        uint32_t window_size = 32;
        // don't do postprocessing around a fixed-sized border, because the window can't fit in the source image
        uint32_t boundary_skip_size = window_size / img->block_size;
        // expand boundary even more to speed up (optional)
        boundary_skip_size *= 2;

        // copy the border
        dim3 block_size{16, 16};
        dim3 grid_size{(orig_vecs->width + block_size.x - 1) / block_size.x,
                       (2 * boundary_skip_size + block_size.y - 1) / block_size.y};
        // copy top and bottom border, including all 4 corners
        copy_border_top_bottom<<<grid_size, block_size>>>(*orig_vecs, out->ref(), boundary_skip_size);

        // copy the columns on the left and right side, but not the corners
        if (orig_vecs->height > 2 * boundary_skip_size) {
            grid_size = dim3{(2 * boundary_skip_size + block_size.x - 1) / block_size.x,
                             (orig_vecs->height - 2 * boundary_skip_size + block_size.y - 1) / block_size.y};
            copy_border_sides<<<grid_size, block_size>>>(*orig_vecs, out->ref(), boundary_skip_size);
        }

        if (2 * boundary_skip_size < orig_vecs->width && 2 * boundary_skip_size < orig_vecs->height) {
            // check that the image isn't so small that there is no region outside the boundary
            grid_size = dim3{(orig_vecs->width - 2 * boundary_skip_size + block_size.x - 1) / block_size.x,
                             (orig_vecs->height - 2 * boundary_skip_size + block_size.y - 1) / block_size.y};
            refine<<<grid_size, block_size>>>(this->last_image->GetGpuImageRef(), img->GetGpuImageRef(),
                                              *orig_vecs, img->block_size, out->ref(), window_size, boundary_skip_size);
        }
    }

    this->last_image = img;

    this->push_blocking(img);
}

void SubPixelPostProcess::on_thread_stop() {
    this->last_image.reset();
}

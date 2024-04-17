#include "ConvertToFloat.h"

#include "GLUtils.h"
#include <cuda_runtime.h>
#include "CudaImage.h"

using namespace std;

// convert "S10.5" flow vectors (int16s with the first 10 bits as integer part, last 5 bits as a fractional part)
// to floating point representation
__global__
void s105_vec_to_float_image(CudaImageRef<S105Vector> s105_vec_image, CudaImageRef<Point<float>> float_img) {
    uint32_t x = blockIdx.x * blockDim.x + threadIdx.x;
    uint32_t y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < s105_vec_image.width && y < s105_vec_image.height) {
        float_img.write({x, y}, s105_to_point_float(s105_vec_image.read({x, y})));
    }
}

/*__global__
void uint8_to_float(CudaImageRef<uint8_t> uint8_img, CudaImageRef<float> float_img) {
    uint32_t x = blockIdx.x * blockDim.x + threadIdx.x;
    uint32_t y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < uint8_img.width && y < uint8_img.height) {
        float_img.write({x, y}, static_cast<float>(uint8_img.read({x, y})));
    }
}*/

void ConvertToFloat::process_image(const std::shared_ptr<OpticalFlowImage> &img) {
    /*{
        auto uint8_img = img->GetGpuImageRef();
        img->float_img = std::make_shared<CudaImageOwned<float, 1>>(uint8_img.width, uint8_img.height);

        dim3 block_size(16, 16);
        dim3 grid_size((uint8_img.width + block_size.x - 1) / block_size.x, (uint8_img.height + block_size.y - 1) / block_size.y);
        uint8_to_float<<<grid_size, block_size>>>(uint8_img, img->float_img->ref());
    }*/

    auto s105_vec_image = img->GetGpuFlowVectorsRef();
    if (s105_vec_image) {
        img->float_vecs = std::make_shared<CudaImageOwned<Point<float>>>(s105_vec_image->width, s105_vec_image->height);

        dim3 block_size(16, 16);
        dim3 grid_size((s105_vec_image->width + block_size.x - 1) / block_size.x,
                       (s105_vec_image->height + block_size.y - 1) / block_size.y);
        s105_vec_to_float_image<<<grid_size, block_size>>>(*s105_vec_image, img->float_vecs->ref());
    }
}

#include "OpticalFlowImage.h"

#include "GLRenderer.h"

void OpticalFlowImage::GLUploadSourceImage(GLRenderer &renderer) {
    renderer.image_texture.UpdateParams((int) this->gpu_image_nv->getWidth(), (int) this->gpu_image_nv->getHeight(), GL_R8);

    if (renderer.image_texture.cuda_resource) {
        renderer.image_texture.CopyFromDevicePtr(dynamic_cast<NvOFBufferCudaDevicePtr*>(this->gpu_image_nv.get()), renderer.streams[0]);
    } else {
        this->cpu_image->GLUploadSourceImage(renderer);
    }
}

// I is intermediate summation type
template <typename T>
static std::shared_ptr<CPUImageOwned<Point<float>>> downsample(
        std::shared_ptr<CPUImageOwned<Point<T>>> orig, uint32_t downsample_factor, float scale_factor) {
    uint32_t downsampled_width = orig->width / downsample_factor;
    uint32_t downsampled_height = orig->height / downsample_factor;

    auto out = std::make_shared<CPUImageOwned<Point<float>>>(downsampled_width, downsampled_height);
    for (uint32_t xbase = 0; xbase < downsampled_width; xbase++) {
        for (uint32_t ybase = 0; ybase < downsampled_height; ybase++) {
            float usum = 0, vsum = 0;
            for (uint32_t xoff = 0; xoff < downsample_factor; xoff++) {
                for (uint32_t yoff = 0; yoff < downsample_factor; yoff++) {
                    uint32_t x = xbase * downsample_factor + xoff;
                    uint32_t y = ybase * downsample_factor + yoff;
                    auto pt = orig->read({x, y});
                    usum += pt.x;
                    vsum += pt.y;
                }
            }
            auto n = static_cast<float>(downsample_factor * downsample_factor);
            out->write({xbase, ybase}, {static_cast<float>(usum) / n * scale_factor,
                                        static_cast<float>(vsum) / n * scale_factor});
        }
    }
    return out;
}

void OpticalFlowImage::GLUploadVectorsVAO(GLRenderer &renderer) {
    if (!this->gpu_flow_vectors_nv) {
        return;
    }

    std::shared_ptr<CPUImageOwned<Point<float>>> downsampled;
    if (this->float_vecs) {
        // refined
        auto float_vecs_cpu = this->float_vecs->ref().download();
        downsampled = downsample(float_vecs_cpu, renderer.flow_vec_downsample, 1.0f);
    } else {
        // no refining enabled
        auto s105_vecs_cpu = this->GetCpuFlowVectors();
        downsampled = downsample(s105_vecs_cpu, renderer.flow_vec_downsample, 1.0f / 32.0f);
    }
    GLsizeiptr size = downsampled->width * downsampled->height * sizeof(Point<float>);
    glBindBuffer(GL_ARRAY_BUFFER, renderer.arrows_vbo);
    glBufferData(GL_ARRAY_BUFFER, size, downsampled->data, GL_DYNAMIC_DRAW);
}

void OpticalFlowImage::GLUploadVectorsTexture(GLRenderer &renderer) {
    if (!this->gpu_flow_vectors_nv) {
        return;
    }

    renderer.image_texture.UpdateParams((int) this->gpu_flow_vectors_nv->getWidth(), (int) this->gpu_flow_vectors_nv->getHeight(), GL_RG32F);
    this->float_vecs->ref().download()->GLUploadSourceImage(renderer);
    // copying from cuda into RG16_SNORM appears unsupported (fails to register cuda graphics resource)
    // we could convert to another format or use GL_RG16I with isampler2D, but the performance boost would be pretty small
    //this->GetCpuFlowVectors()->GLUploadSourceImage(renderer);
}

std::shared_ptr<CPUImageOwned<S105Vector>> OpticalFlowImage::GetCpuFlowVectors() {
    if (!this->gpu_flow_vectors_nv) {
        // first image does not have any vectors
        return nullptr;
    }

    if (this->cpu_flow_vectors_cached) {
        // already have
        return this->cpu_flow_vectors_cached;
    } else {
        std::unique_lock lock(this->cpu_flow_mutex);
        if (!this->cpu_flow_vectors_cached) {
            // we are the fastest thread in race
            size_t size = this->gpu_flow_vectors_nv->getWidth() * this->gpu_flow_vectors_nv->getHeight() * this->gpu_flow_vectors_nv->getElementSize();
            void *data = malloc(size);
            if (!data) {
                throw std::bad_alloc();
            }
            this->gpu_flow_vectors_nv->DownloadData(data);
            this->cpu_flow_vectors_cached = std::make_shared<CPUImageOwned<S105Vector>>(this->gpu_flow_vectors_nv->getWidth(), this->gpu_flow_vectors_nv->getHeight(), data);
        }
        return this->cpu_flow_vectors_cached;
    }
}

CudaImageRef<uint8_t> OpticalFlowImage::GetGpuImageRef() const {
    return {this->gpu_image_nv};
}

std::optional<CudaImageRef<S105Vector>> OpticalFlowImage::GetGpuFlowVectorsRef() const {
    if (this->gpu_flow_vectors_nv) {
        return {this->gpu_flow_vectors_nv};
    } else {
        return std::nullopt;
    }
}
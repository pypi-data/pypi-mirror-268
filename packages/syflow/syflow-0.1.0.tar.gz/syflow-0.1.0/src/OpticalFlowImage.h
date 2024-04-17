#pragma once

#include "vendor/nvof/NvOFCuda.h"
#include <optional>
#include <mutex>
#include "CudaImage.h"

class OpticalFlowImage {
public:
    uint32_t block_size{};

    std::shared_ptr<NvOFCuda> nvof;
    std::shared_ptr<CPUImageOwned<uint8_t>> cpu_image;
    std::shared_ptr<NvOFBuffer> gpu_image_nv;
    /// flow vectors calculated between the previous image and this image.
    /// null for the first image.
    std::shared_ptr<NvOFBuffer> gpu_flow_vectors_nv;

    std::shared_ptr<CudaImageOwned<Point<float>>> float_vecs;

    [[nodiscard]] CudaImageRef<uint8_t> GetGpuImageRef() const;
    [[nodiscard]] std::optional<CudaImageRef<S105Vector>> GetGpuFlowVectorsRef() const;

    void GLUploadSourceImage(GLRenderer &renderer);
    // upload flow vectors into vertex array object, and downsample with factor of renderer.flow_vec_downsample
    void GLUploadVectorsVAO(GLRenderer &renderer);
    // upload flow vectors into opengl texture
    void GLUploadVectorsTexture(GLRenderer &renderer);

    // downloads if not already on the CPU
    std::shared_ptr<CPUImageOwned<S105Vector>> GetCpuFlowVectors();
private:
    std::mutex cpu_flow_mutex;
    std::shared_ptr<CPUImageOwned<S105Vector>> cpu_flow_vectors_cached;
};
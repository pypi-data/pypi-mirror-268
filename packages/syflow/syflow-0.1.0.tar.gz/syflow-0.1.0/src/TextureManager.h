#pragma once

#include <glad/glad.h>
#include <cuda.h>
#include <cuda_gl_interop.h>
#include "vendor/nvof/NvOFCuda.h"

class TextureManager {
public:
    void UpdateParams(int width, int height, int gl_internal_format);
    void CopyFromDevicePtr(NvOFBufferCudaDevicePtr *src, cudaStream_t stream);
    unsigned int current_width{}, current_height{}, current_internal_format{}, texture_id{};
    cudaGraphicsResource_t cuda_resource{nullptr};
    ~TextureManager();
};

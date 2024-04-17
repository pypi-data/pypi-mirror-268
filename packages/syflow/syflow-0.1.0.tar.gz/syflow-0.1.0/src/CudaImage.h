#pragma once

#include "Point.h"
#include "GLUtils.h"
#include "vendor/nvof/NvOFCuda.h"
#include "CPUImageOwned.h"

// signed short with 10 integer bits and 5 fractional bits, vector with U and V component
using S105Vector = Point<int16_t>;


// round to nearest int
__device__ [[nodiscard]] PointI32 s105_to_point_rounded(Point<int16_t> s105_pt);
__device__ [[nodiscard]] Point<float> s105_to_point_float(Point<int16_t> s105_pt);

template <typename T>
struct CudaImageRef {
    T* device_ptr{};
    uint32_t width{};
    uint32_t height{};
    /// bytes to skip to go to next row
    uint32_t pitch{};

    __device__ T* get_addr(PointU32 p) const {
        return ((T*) (((uint8_t*) device_ptr) + pitch * p.y) + p.x);
    }

    __device__ T read(PointU32 p) const {
        return *this->get_addr(p);
    }

    __device__ T write(PointU32 p, T val) {
        *this->get_addr(p) = val;
    }

    CudaImageRef(uint32_t width, uint32_t height, uint32_t pitch, T* device_ptr): width(width), height(height), pitch(pitch), device_ptr(device_ptr) {}

    CudaImageRef(const std::shared_ptr<NvOFBuffer> &buf) {
        auto dev_ptr_buf = std::dynamic_pointer_cast<NvOFBufferCudaDevicePtr>(buf);
        this->width = dev_ptr_buf->getWidth();
        this->height = dev_ptr_buf->getHeight();
        this->pitch = dev_ptr_buf->getStrideInfo().strideInfo[0].strideXInBytes;
        this->device_ptr = reinterpret_cast<T*>(dev_ptr_buf->getCudaDevicePtr());
    }

    std::shared_ptr<CPUImageOwned<T>> download() {
        auto cpu_img = std::make_shared<CPUImageOwned<T>>(this->width, this->height);
        checkCudaRT(cudaMemcpy2D(cpu_img->data, this->width * sizeof(T), this->device_ptr, this->pitch, this->width * sizeof(T), this->height, cudaMemcpyDeviceToHost));
        return cpu_img;
    }
};

// Pitch-linear CUDA device memory which frees on destruction
template <typename T>
class CudaImageOwned {
public:
    uint32_t width, height, pitch;
    T *device_ptr;

    // allocate a pitched image
    // a pitched image has padding at end of rows to optimize memory accesses when running kernels, see `cudaMallocPitch` CUDA docs
    CudaImageOwned(uint32_t width, uint32_t height): width(width), height(height), pitch{} {
        // pitch will never be larger than uint32_t, but cudaMallocPitch API requires size_t
        size_t pitch_sizet;
        checkCudaRT(cudaMallocPitch(&this->device_ptr, &pitch_sizet, width * sizeof(T), height));
        this->pitch = static_cast<uint32_t>(pitch_sizet);
    }
    // create an image object around already-allocated data
    CudaImageOwned(uint32_t width, uint32_t height, uint32_t pitch, void* device_ptr): width(width), height(height), device_ptr(device_ptr), pitch(pitch) {}

    ~CudaImageOwned() {
        checkCudaRT(cudaFree(this->device_ptr));
    }

    CudaImageOwned(const CudaImageOwned &) = delete;
    CudaImageOwned& operator=(const CudaImageOwned &) = delete;

    [[nodiscard]] CudaImageRef<T> ref() {
        return {width, height, pitch, device_ptr};
    }
};
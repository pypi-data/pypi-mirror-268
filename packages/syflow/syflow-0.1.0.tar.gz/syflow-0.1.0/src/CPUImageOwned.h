#pragma once

#include <cstdint>
#include <cstdlib>
#include "Point.h"

class GLRenderer;

template <typename T>
class CPUImageOwned {
public:
    uint32_t width, height;
    T* data;

    CPUImageOwned(uint32_t width, uint32_t height): width(width), height(height) {
        this->data = (T*) malloc(width * sizeof(T) * height);
    }
    CPUImageOwned(uint32_t width, uint32_t height, void* data): width(width), height(height), data((T*) data) {}

    virtual ~CPUImageOwned() {
        free(this->data);
    }

    CPUImageOwned(const CPUImageOwned &) = delete;
    CPUImageOwned& operator=(const CPUImageOwned &) = delete;

    T read(PointU32 p) {
        return data[p.y * width + p.x];
    }

    void write(PointU32 p, T val) {
        data[p.y * width + p.x] = val;
    }

    uint32_t PixelSize() {
        return sizeof(T);
    }

    void GLUploadSourceImage(GLRenderer &renderer);
};
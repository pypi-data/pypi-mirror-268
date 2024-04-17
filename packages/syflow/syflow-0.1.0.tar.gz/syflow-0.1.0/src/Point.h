#pragma once

#include <cuda_runtime.h>
#include <cstdint>

template <typename T>
struct Point {
    T x;
    T y;

    __host__ __device__ Point operator+ (const Point &other) const {
        return {this->x + other.x, this->y + other.y};
    }

    __host__ __device__ Point operator- (const Point &other) const {
        return {this->x - other.x, this->y - other.y};
    }
};
using PointU32 = Point<uint32_t>;
using PointI32 = Point<int32_t>;
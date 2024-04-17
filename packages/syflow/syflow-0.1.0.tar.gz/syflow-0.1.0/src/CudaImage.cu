#include "CudaImage.h"

__device__ [[nodiscard]] Point<float> s105_to_point_float(Point<int16_t> s105_pt) {
    return {static_cast<float>(s105_pt.x) / 32.0f, static_cast<float>(s105_pt.y) / 32.0f};
}

__device__ [[nodiscard]] PointI32 s105_to_point_rounded(Point<int16_t> s105_pt) {
    return {((int32_t) s105_pt.x + 16) / 32, ((int32_t) s105_pt.y + 16) / 32};
}
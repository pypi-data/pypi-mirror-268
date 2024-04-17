#pragma once

#include "Pipeline.h"

class ConvertToFloat: public ImageProcessor {
public:
    void process_image(const std::shared_ptr<OpticalFlowImage> &img) override;
};

#pragma once

#include "Pipeline.h"

class OpticalFlowSaver : public ImageProcessor {
public:
    // force disable
    bool user_disabled{false};

    std::string dir;
    size_t file_num = 0;

    OpticalFlowSaver(std::string dir = "");

    // disabled if no directory set, or user force disabled
    bool disabled() override;
protected:
    void process_image(const std::shared_ptr<OpticalFlowImage> &img) override;
};
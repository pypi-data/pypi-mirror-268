#pragma once

#include "Pipeline.h"
#include "OpticalFlowUploader.h"

class SubPixelPostProcess: public ImageProcessor {
private:
    std::shared_ptr<OpticalFlowImage> last_image;
public:
    void process_image(const std::shared_ptr<OpticalFlowImage> &img) override;
    void on_thread_stop() override;
};

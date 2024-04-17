#pragma once

#include "OpticalFlowUploader.h"

class OpticalFlowExecutor : public ImageProcessor {
protected:
    void process_image(const std::shared_ptr<OpticalFlowImage> &image) override;
    void on_thread_stop() override;
private:
    std::shared_ptr<OpticalFlowImage> last_image;
};

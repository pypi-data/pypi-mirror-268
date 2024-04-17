#pragma once

#include "Pipeline.h"
#include "vendor/nvof/NvOFCuda.h"
#include <optional>
#include <mutex>
#include "CudaImage.h"

// uploader creates the NvOFCuda object and uploads images from CPU to GPU
class OpticalFlowUploader : public ImageProcessor {
public:
	// block size 1, 2, or 4
	OpticalFlowUploader(CUcontext cuContext, int block_size);
    // use current thread's cuda context
    OpticalFlowUploader(int block_size);

    void on_thread_start() override;
	void process_image(const std::shared_ptr<OpticalFlowImage> &image) override;
private:
	CUcontext cuContext = nullptr;
	std::shared_ptr<NvOFCuda> nvof;
	uint32_t width{}, height{}, block_size{};
	void init_nvof();
};
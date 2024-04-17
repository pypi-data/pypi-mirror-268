#include "OpticalFlowUploader.h"
#include "Log.h"
#include "GLUtils.h"
#include "GLRenderer.h"
#include <npp.h>

using namespace std;

OpticalFlowUploader::OpticalFlowUploader(CUcontext cuContext, int block_size) : cuContext(cuContext), block_size(block_size) {}

OpticalFlowUploader::OpticalFlowUploader(int block_size): block_size(block_size) {
    checkCudaDrv(cuCtxGetCurrent(&this->cuContext));
}

void OpticalFlowUploader::on_thread_start() {
    ImageProcessor::on_thread_start();

    // we need to delay NvOF initialization until we know the image dimensions
    this->width = 0;
    this->height = 0;
}

void OpticalFlowUploader::process_image(const std::shared_ptr<OpticalFlowImage> &img) {
    if (this->width != img->cpu_image->width || this->height != img->cpu_image->height) {
        // need to reinitialize if dimensions change and on first image
        this->width = img->cpu_image->width;
        this->height = img->cpu_image->height;
        this->init_nvof();
    }

    img->nvof = this->nvof;
    img->block_size = this->block_size;
    img->gpu_image_nv = std::move(this->nvof->CreateBuffers(NV_OF_BUFFER_USAGE_INPUT, 1)[0]);
    img->gpu_image_nv->UploadData(img->cpu_image->data);
}

void OpticalFlowUploader::init_nvof() {
    CUstream inputStream = nullptr;
    CUstream outputStream = nullptr;
    // I measured same performance with cuDeivcePtr and cuArray using AppOFCuda from optical flow SDK samples
    NV_OF_CUDA_BUFFER_TYPE inputBufferType = NV_OF_CUDA_BUFFER_TYPE_CUDEVICEPTR;
    NV_OF_CUDA_BUFFER_TYPE outputBufferType = NV_OF_CUDA_BUFFER_TYPE_CUDEVICEPTR;
    NV_OF_PERF_LEVEL perfPreset = NV_OF_PERF_LEVEL_MEDIUM;
    this->nvof = dynamic_pointer_cast<NvOFCuda>(shared_ptr(
            NvOFCuda::Create(this->cuContext, this->width, this->height, NV_OF_BUFFER_FORMAT_GRAYSCALE8, inputBufferType, outputBufferType, NV_OF_MODE_OPTICALFLOW, perfPreset, inputStream, outputStream
            )));
    this->nvof->Init(this->block_size);
}
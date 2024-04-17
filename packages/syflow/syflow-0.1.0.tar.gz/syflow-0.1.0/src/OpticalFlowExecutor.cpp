#include "OpticalFlowExecutor.h"

using namespace std;

void OpticalFlowExecutor::process_image(const std::shared_ptr<OpticalFlowImage> &img) {
    // we need previous image to calculate flow vectors for this image
    if (this->last_image && this->last_image->nvof == img->nvof) {
        // allocate flow vector buffer on gpu
        img->gpu_flow_vectors_nv = std::move(img->nvof->CreateBuffers(NV_OF_BUFFER_USAGE_OUTPUT, 1)[0]);

        // execute optical flow
        img->nvof->Execute(this->last_image->gpu_image_nv.get(), img->gpu_image_nv.get(), img->gpu_flow_vectors_nv.get());

        // download flow vectors to cpu
        //auto cpu_output = make_shared<NV_OF_FLOW_VECTOR[]>(this->height * this->width);
        //output_gpu_buffer->DownloadData(cpu_output.get());
    }

    this->last_image = img;
}

void OpticalFlowExecutor::on_thread_stop() {
    this->last_image.reset();
}

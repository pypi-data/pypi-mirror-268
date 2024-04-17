#include "OpticalFlowSaver.h"
#include "Log.h"

#include <utility>
#include <fstream>

OpticalFlowSaver::OpticalFlowSaver(std::string dir): dir(std::move(dir)) {}

void OpticalFlowSaver::process_image(const std::shared_ptr<OpticalFlowImage> &img) {
    auto opt_flow_img = dynamic_cast<OpticalFlowImage*>(img.get());
    if (!opt_flow_img) {
        throw std::invalid_argument("optical flow saver received unknown image type");
    }
    auto cpu_flow_vecs = opt_flow_img->GetCpuFlowVectors();
    if (cpu_flow_vecs) {
        auto filename = this->dir + "/flow_" + std::to_string(this->file_num++) + ".nvof";

        std::ofstream out(filename, std::ios::binary);
        out.write((const char*) cpu_flow_vecs->data, (std::streamsize) cpu_flow_vecs->width * cpu_flow_vecs->height * cpu_flow_vecs->PixelSize());
        out.close();
    }
}

bool OpticalFlowSaver::disabled() {
    return this->user_disabled || this->dir.empty();
}

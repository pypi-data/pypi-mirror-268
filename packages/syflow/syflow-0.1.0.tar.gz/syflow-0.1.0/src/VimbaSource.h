#pragma once

#include "CameraAPI.h"
#include "Pipeline.h"
#include <VimbaCPP/Include/VimbaCPP.h>

class VimbaAPI : public CameraAPI {
    std::string getAPIName() override;
    std::vector<std::shared_ptr<CameraSource>> getCameras() override;
};

class VimbaSource : public CameraSource {
private:
    AVT::VmbAPI::CameraPtr camera;
    size_t num_frame_bufs{10};
    AVT::VmbAPI::FramePtrVector frame_bufs;
public:
    VimbaSource(const AVT::VmbAPI::CameraPtr& camera);
    std::string getName() override;
    std::string getDescription() override;
    void run_thread() override;
    void on_thread_stop() override;
};
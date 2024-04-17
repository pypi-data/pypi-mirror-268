#include <map>
#include <string>
#include "Log.h"
#include "VimbaSource.h"
#include "CPUImageOwned.h"
#include <cstring>

using namespace AVT::VmbAPI;
using namespace std;

static std::map<VmbError_t, string> VIMBA_ERROR_NAMES = {
    {VmbErrorSuccess, "VmbErrorSuccess"},
    {VmbErrorInternalFault, "VmbErrorInternalFault"},
    {VmbErrorApiNotStarted, "VmbErrorApiNotStarted"},
    {VmbErrorNotFound, "VmbErrorNotFound"},
    {VmbErrorBadHandle, "VmbErrorBadHandle"},
    {VmbErrorDeviceNotOpen, "VmbErrorDeviceNotOpen"},
    {VmbErrorInvalidAccess, "VmbErrorInvalidAccess"},
    {VmbErrorBadParameter, "VmbErrorBadParameter"},
    {VmbErrorStructSize, "VmbErrorStructSize"},
    {VmbErrorMoreData, "VmbErrorMoreData"},
    {VmbErrorWrongType, "VmbErrorWrongType"},
    {VmbErrorInvalidValue, "VmbErrorInvalidValue"},
    {VmbErrorTimeout, "VmbErrorTimeout"},
    {VmbErrorOther, "VmbErrorOther"},
    {VmbErrorResources, "VmbErrorResources"},
    {VmbErrorInvalidCall, "VmbErrorInvalidCall"},
    {VmbErrorNoTL, "VmbErrorNoTL"},
    {VmbErrorNotImplemented, "VmbErrorNotImplemented"},
    {VmbErrorNotSupported, "VmbErrorNotSupported"},
    {VmbErrorIncomplete, "VmbErrorIncomplete"},
    {VmbErrorIO, "VmbErrorIO"}
};

static void vimba_error_check_func(VmbError_t error, const std::string &msg) {
    if (error != VmbErrorSuccess) {
        auto error_name_it = VIMBA_ERROR_NAMES.find(error);
        string error_name = error_name_it == VIMBA_ERROR_NAMES.end() ? ("error " + std::to_string(error)) : error_name_it->second;
        throw std::runtime_error(msg + ": " + error_name);
    }
}

#define vimba_error_check(error) vimba_error_check_func(error, std::string(__FILE__) + ":" + std::to_string(__LINE__))

std::string VimbaAPI::getAPIName() {
    return "Vimba";
}

std::vector<std::shared_ptr<CameraSource>> VimbaAPI::getCameras() {
    VimbaSystem &sys = VimbaSystem::GetInstance();
    vimba_error_check(sys.Startup());

    CameraPtrVector cameras;
    vimba_error_check(sys.GetCameras(cameras));

    std::vector<std::shared_ptr<CameraSource>> infos;
    for (auto &camera: cameras) {
        infos.push_back(std::make_shared<VimbaSource>(camera));
    }
    return infos;
}

class FrameObserver : public IFrameObserver {
    VimbaSource *output;

    public:
    FrameObserver(const CameraPtr& pCamera, VimbaSource* output) : IFrameObserver(pCamera), output(output) {}
    void FrameReceived(const FramePtr pFrame) override
    {
        VmbUint32_t width, height;
        vimba_error_check(pFrame->GetWidth(width));
        vimba_error_check(pFrame->GetHeight(height));
        // this frame received method must process quickly, because if it is too slow,
        // the camera acquisition will reduce frame rate

        VmbUchar_t *buf;
        vimba_error_check(pFrame->GetBuffer(buf));

        // todo: make a custom Image class that automatically re-queues the frame when not needed anymore
        // this would prevent this unnecessary copy
        void* copy = malloc(width * height);
        memcpy(copy, buf, width * height);

        auto opt_flow_img = std::make_shared<OpticalFlowImage>();
        opt_flow_img->cpu_image = std::make_shared<CPUImageOwned<uint8_t>>(width, height, copy);
        output->push_nonblocking(opt_flow_img);

        // requeue frame to allow the buffer to be re-used
        m_pCamera->QueueFrame(pFrame);
    }
};

void VimbaSource::run_thread() {
    Log() << "vimba open " << this->getName();
    vimba_error_check(camera->Open(VmbAccessModeFull));
    Log() << "vimba open camera success" ;
    
    // Get the image size for the required buffer
    FeaturePtr pFeature;
    VmbInt64_t payload_size;
    vimba_error_check(camera->GetFeatureByName("PayloadSize", pFeature));
    vimba_error_check(pFeature->GetValue(payload_size));
    Log() << "payload size " << payload_size ;

    this->frame_bufs.clear();
    IFrameObserverPtr observer{new FrameObserver(camera, this)};
    for (size_t i = 0; i < this->num_frame_bufs; i++) {
        // Allocate memory for frame buffer
        // Register frame observer / callback for each frame
        // Announce frame to the API
        FramePtr frame{new Frame(payload_size)};
        frame->RegisterObserver(observer);
        camera->AnnounceFrame(frame);
        this->frame_bufs.push_back(frame);
    }
    Log() << "vimba StartCapture";
    camera->StartCapture();
    for (auto &frame : this->frame_bufs)
    {
        camera->QueueFrame(frame);
    }

    Log() << "vimba AcquisitionStart";
    camera->GetFeatureByName("AcquisitionStart", pFeature);
    pFeature->RunCommand();
}

void VimbaSource::on_thread_stop() {
    Log() << "vimba AcquisitionStop";
    FeaturePtr pFeature;
    camera->GetFeatureByName("AcquisitionStop", pFeature);
    pFeature->RunCommand();
    Log() << "vimba EndCapture";
    camera->EndCapture();
    camera->FlushQueue();
    camera->RevokeAllFrames();
    for (auto &frame : this->frame_bufs) {
        frame->UnregisterObserver();
    }
    this->frame_bufs.clear();
    camera->Close();
    Log() << "vimba closed";
}

VimbaSource::VimbaSource(const AVT::VmbAPI::CameraPtr& camera): camera(camera) {}

std::string VimbaSource::getName() {
    std::string name;
    vimba_error_check(this->camera->GetName(name));
    return name;
}

std::string VimbaSource::getDescription() {
    std::string id;
    vimba_error_check(this->camera->GetID(id));
    std::string interface_id;
    vimba_error_check(this->camera->GetInterfaceID(interface_id));
    std::string serial_number;
    vimba_error_check(this->camera->GetSerialNumber(serial_number));
    return "Serial: " + serial_number + "\n" + \
           "Interface: " + interface_id + "\n" + \
           "ID: " + id;
}
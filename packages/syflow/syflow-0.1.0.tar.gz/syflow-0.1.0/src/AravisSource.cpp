#include "AravisSource.h"

#include <arv.h>

class AravisError : public std::exception {
    int code;
    std::string message;
public:
    AravisError(GError *error) {
        code = error->code;
        message = error->message;
    }
    [[nodiscard]] const char *what() const noexcept override {
        return message.c_str();
    }
};

std::string AravisAPI::getAPIName() {
    return "Aravis";
}

std::vector<std::shared_ptr<CameraSource>> AravisAPI::getCameras() {
    arv_update_device_list();

    unsigned int n_devices = arv_get_n_devices();
    std::vector<std::shared_ptr<CameraSource>> infos;
    for (unsigned int i = 0; i < n_devices; i++) {
        infos.push_back(std::make_shared<AravisSource>(i));
    }
    return infos;
}

AravisSource::AravisSource(unsigned int index): index(index) {}

static std::string string_or_null(const char* str) {
    if (str == nullptr) {
        return "null";
    } else {
        return {str};
    }
}

std::string AravisSource::getName() {
    std::string model = string_or_null(arv_get_device_model(this->index));
    std::string vendor = string_or_null(arv_get_device_vendor(this->index));
    return vendor + " " + model;
}

std::string AravisSource::getDescription() {
    std::string model = string_or_null(arv_get_device_model(this->index));
    std::string protocol = string_or_null(arv_get_device_protocol(this->index));
    std::string serial_nbr = string_or_null(arv_get_device_serial_nbr(this->index));
    std::string vendor = string_or_null(arv_get_device_vendor(this->index));
    return "Vendor: " + vendor + "\n"
           "Model: " + model + "\n" +
           "Protocol: " + protocol + "\n" +
           "Serial Number: " + serial_nbr;
}

static void internal_checkErrorsArv(const char *file, int line, GError *error) {
    if (error != nullptr) {
        Log() << "Aravis error at " << file << ":" << line << " code = " << error->code << " (" << error->message << ")";
        throw AravisError(error);
    }
}

#define checkArv(gerror) internal_checkErrorsArv(__FILE__, __LINE__, gerror)

void AravisSource::run_thread() {
    const char *id = arv_get_device_id(this->index);
    GError *error = nullptr;
    Log() << "open camera " << id;
    auto device = arv_camera_new(id, &error);
    checkArv(error);

    if (!ARV_IS_CAMERA(device)) {
        Log() << "device " << id << " is not a camera";
        return;
    }

    Log() << "set acquisition mode";
    arv_camera_set_acquisition_mode(device, ARV_ACQUISITION_MODE_CONTINUOUS, &error);
    checkArv(error);

    Log() << "create stream";
    auto stream = arv_camera_create_stream(device, nullptr, nullptr, &error);
    checkArv(error);

    // see https://github.com/AravisProject/aravis-c-examples/blob/main/02-multiple-acquisition-main-thread.c
    size_t payload = arv_camera_get_payload(device, &error);
    checkArv(error);

    for (size_t i = 0; i < 2; i++) {
        arv_stream_push_buffer(stream, arv_buffer_new(payload, nullptr));
    }

    Log() << "start acquistion";
    arv_camera_start_acquisition(device, &error);
    checkArv(error);

    while (this->keep_running.load()) {
        Log() << "wait for buf";
        auto buf = arv_stream_pop_buffer(stream);
        Log() << "got buf";
        if (ARV_IS_BUFFER(buf)) {
            // todo no copy
            size_t size = 0;
            const void *img_data = arv_buffer_get_data(buf, &size);
            auto copy = malloc(size);

            uint32_t width = arv_buffer_get_image_width(buf);
            uint32_t height = arv_buffer_get_image_height(buf);
            memcpy(copy, img_data, width * height);

            auto opt_flow_img = std::make_shared<OpticalFlowImage>();
            opt_flow_img->cpu_image = std::make_shared<CPUImageOwned<uint8_t>>(width, height, copy);
            this->push_nonblocking(opt_flow_img);

            arv_stream_push_buffer(stream, buf);
        }
    }

    g_object_unref(stream);

    arv_camera_stop_acquisition(device, &error);
    checkArv(error);

    g_object_unref(device);
}

void AravisSource::on_thread_stop() {

}

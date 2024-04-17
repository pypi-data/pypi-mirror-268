#pragma once

#include "CameraAPI.h"

class AravisAPI : public CameraAPI {
    std::string getAPIName() override;
    std::vector<std::shared_ptr<CameraSource>> getCameras() override;
};

class AravisSource : public CameraSource {
private:
    unsigned int index;
public:
    AravisSource(unsigned int index);
    std::string getName() override;
    std::string getDescription() override;
    void run_thread() override;
    void on_thread_stop() override;
};
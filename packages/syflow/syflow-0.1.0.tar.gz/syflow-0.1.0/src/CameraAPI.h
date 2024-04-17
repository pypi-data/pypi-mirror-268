#pragma once

#include <string>
#include <vector>
#include "Pipeline.h"

class CameraSource : public ImageSource {
public:
    // get the name of this camera
    virtual std::string getName() = 0;
    // user-facing description for camera chooser gui
    virtual std::string getDescription() = 0;
};

// A singleton object representing a camera API, such as Genicam or V4L2
class CameraAPI {
public:
    // get the name of the Camera API
    virtual std::string getAPIName() = 0;
    virtual std::vector<std::shared_ptr<CameraSource>> getCameras() = 0;

    // return instances of all APIs
    static std::vector<CameraAPI*> &getAPIs();
};
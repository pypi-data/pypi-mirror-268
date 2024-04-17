#include "CameraAPI.h"
#ifdef ENABLE_VIMBA
#include "VimbaSource.h"
#endif
#ifdef ENABLE_ARAVIS
#include "AravisSource.h"
#endif

static std::vector<CameraAPI*> camera_apis;

std::vector<CameraAPI*> &CameraAPI::getAPIs() {
    if (camera_apis.empty()) {
#ifdef SYFLOW_ENABLE_VIMBA
        camera_apis.push_back(new VimbaAPI());
#endif
#ifdef SYFLOW_ENABLE_ARAVIS
        camera_apis.push_back(new AravisAPI());
#endif
    }
    return camera_apis;
}

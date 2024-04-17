#include <memory>
#include "Log.h"
#include "Pipeline.h"
#include "vendor/nvof/NvOFCuda.h"
#include <sstream>
#include <optional>

#include "vendor/portable-file-dialogs.h"
#include "GLRenderer.h"
#include "VimbaSource.h"
#include "gui/GUIWindow.h"
#include "gui/SourceChooserGUI.h"
#include "gui/DisplayOptionsGUI.h"
#include "gui/ControlGUI.h"
#include "OpticalFlowUploader.h"
#include "OpticalFlowExecutor.h"
#include "OpticalFlowSaver.h"
#include "gui/SaverOptionsGUI.h"
#include "ConvertToFloat.h"
#include "SubPixelPostProcess.h"
#include "gui/PostProcessGUI.h"

#pragma clang diagnostic push
#pragma ide diagnostic ignored "NullDereference"
#ifdef _WIN32
#include "winuser.h"
// prefer nvidia gpu over integrated graphics https://stackoverflow.com/a/68471374
__declspec(dllexport) DWORD NvOptimusEnablement = 1;
#endif

using namespace std;

#ifdef _WIN32
int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd) {
#else
int main() {
#endif
/*#ifdef _WIN32
    // enable support for HiDPI screens
    SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2);
#endif
*/

    // show window as quick as possible
    GUIWindow window;
    window.Show(1200, 800);

    // initialize cuda
    CUcontext cuContext;
    CUdevice cuDevice = 0; // if multiple GPUs, use the first. could allow user to change

    cudaDeviceProp prop{};
    cudaGetDeviceProperties(&prop, cuDevice);
    Log() << "init cuda device " << prop.name;

    CUDA_DRVAPI_CALL(cuInit(0));
    CUDA_DRVAPI_CALL(cuCtxCreate(&cuContext, 0, cuDevice));

    auto pipeline = make_shared<Pipeline>();
    auto renderer = make_shared<GLRenderer>();
    pipeline->processors.push_back(std::make_shared<OpticalFlowUploader>(cuContext, 4));
    pipeline->processors.push_back(std::make_shared<OpticalFlowExecutor>());
    pipeline->processors.push_back(std::make_shared<ConvertToFloat>());
    auto post_processor = std::make_shared<SubPixelPostProcess>();
    pipeline->processors.push_back(post_processor);
    auto saver = make_shared<OpticalFlowSaver>();
    pipeline->processors.push_back(saver);
    pipeline->sink = renderer;

    window.components.push_back(make_shared<SourceChooserGUI>(pipeline));
    window.components.push_back(make_shared<DisplayOptionsGUI>(renderer));
    window.components.push_back(make_shared<ControlGUI>(pipeline));
    window.components.push_back(make_shared<SaverOptionsGUI>(saver));
    window.components.push_back(make_shared<PostProcessGUI>(post_processor));
    window.components.push_back(renderer);

    window.RunRenderLoop();

    Log() << "window closed";

    if (pipeline->running) {
        pipeline->Stop();
    }

    Log() << "pipeline stopped";
}

#pragma clang diagnostic pop
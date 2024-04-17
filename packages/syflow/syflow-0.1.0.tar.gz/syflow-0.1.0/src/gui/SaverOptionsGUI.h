#pragma once

#include "GUIComponent.h"
#include "../OpticalFlowSaver.h"
#include "../vendor/portable-file-dialogs.h"
#include <optional>

class SaverOptionsGUI: public GUIComponent {
private:
    std::optional<pfd::select_folder> output_folder_select;
    std::shared_ptr<OpticalFlowSaver> saver;
    bool user_enabled{false};
public:
    SaverOptionsGUI(std::shared_ptr<OpticalFlowSaver> saver);
    void drawImGui() override;
};

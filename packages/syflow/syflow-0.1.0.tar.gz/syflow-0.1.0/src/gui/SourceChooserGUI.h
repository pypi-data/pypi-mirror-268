#pragma once

#include <memory>
#include <optional>
#include "GUIComponent.h"
#include "../vendor/portable-file-dialogs.h"
#include "../CameraAPI.h"
#include "../Pipeline.h"

class SourceChooserGUI : public GUIComponent {
private:
    std::optional<pfd::open_file> input_file_chooser;
    std::vector<std::shared_ptr<CameraSource>> camera_options;
    size_t chosen_camera_option{};
    std::shared_ptr<Pipeline> pipeline;
public:
    SourceChooserGUI(std::shared_ptr<Pipeline> pipeline);
    void drawImGui() override;
};

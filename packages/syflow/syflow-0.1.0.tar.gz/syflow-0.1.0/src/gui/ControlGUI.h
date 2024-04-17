#pragma once

#include "GUIComponent.h"
#include "../Pipeline.h"

class ControlGUI: public GUIComponent {
private:
    std::shared_ptr<Pipeline> pipeline;
public:
    ControlGUI(std::shared_ptr<Pipeline> pipeline);
    void drawImGui() override;
};

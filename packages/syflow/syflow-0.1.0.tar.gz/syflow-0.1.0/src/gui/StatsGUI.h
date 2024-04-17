#pragma once

#include <memory>
#include "GUIComponent.h"
#include "../Pipeline.h"

class StatsGUI: public GUIComponent {
private:
    std::shared_ptr<Pipeline> pipeline;
public:
    StatsGUI(std::shared_ptr<Pipeline> pipeline);
    void drawImGui() override;
};
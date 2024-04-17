#pragma once

#include "GUIComponent.h"
#include "../SubPixelPostProcess.h"

class PostProcessGUI: public GUIComponent {
private:
    std::shared_ptr<SubPixelPostProcess> post_processor;
public:
    PostProcessGUI(std::shared_ptr<SubPixelPostProcess> post_processor);
    void drawImGui() override;
};

#pragma once

#include "GUIComponent.h"
#include "../GLRenderer.h"

class DisplayOptionsGUI : public GUIComponent {
private:
    std::shared_ptr<GLRenderer> renderer;
public:
    DisplayOptionsGUI(std::shared_ptr<GLRenderer> renderer);
    void drawImGui() override;
};

#include "PostProcessGUI.h"

#include <imgui.h>

PostProcessGUI::PostProcessGUI(std::shared_ptr<SubPixelPostProcess> post_processor): post_processor(std::move(post_processor)) {}

void PostProcessGUI::drawImGui() {
    ImGui::Begin("Post Processing");

    ImGui::End();
}
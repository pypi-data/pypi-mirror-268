#include "DisplayOptionsGUI.h"

#include "imgui.h"

DisplayOptionsGUI::DisplayOptionsGUI(std::shared_ptr<GLRenderer> renderer): renderer(std::move(renderer)) {}

void DisplayOptionsGUI::drawImGui() {
    ImGui::Begin("Display");

    ImGui::Combo("Field", &this->renderer->display_option, DISPLAY_OPTION_NAMES, DisplayOption::MAX);
    if (ImGui::TreeNode("Arrows")) {
        ImGui::Checkbox("Enable Arrows", &this->renderer->display_arrows);
        ImGui::InputScalar("Downsampling", ImGuiDataType_U32, &this->renderer->flow_vec_downsample);
        ImGui::InputFloat("Scale", &this->renderer->arrows_display_scale);
        ImGui::TreePop();
    }
    ImGui::InputFloat2("Range", this->renderer->display_range);

    ImGui::End();
}
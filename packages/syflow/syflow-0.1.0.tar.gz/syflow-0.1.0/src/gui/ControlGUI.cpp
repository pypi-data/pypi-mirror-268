#include "ControlGUI.h"

#include "imgui.h"
#include "../vendor/portable-file-dialogs.h"

ControlGUI::ControlGUI(std::shared_ptr<Pipeline> pipeline): pipeline(std::move(pipeline)) {}

void ControlGUI::drawImGui() {
    ImGui::Begin("Control");

    if (this->pipeline->running) {
        if (ImGui::Button("Stop")) {
            this->pipeline->Stop();
        }
    } else {
        if (ImGui::Button("Start")) {
            try {
                this->pipeline->Start();
            } catch (const std::exception &ex) {
                pfd::message("Warning", "Failed to start pipeline: " + std::string(ex.what()), pfd::choice::ok);
            }
        }
    }

    ImGui::End();
}
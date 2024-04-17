#include "SaverOptionsGUI.h"

#include "imgui.h"
#include "../Log.h"

SaverOptionsGUI::SaverOptionsGUI(std::shared_ptr<OpticalFlowSaver> saver): saver(std::move(saver)) {}

void SaverOptionsGUI::drawImGui() {
    ImGui::Begin("Saver Options");

    if (ImGui::Checkbox("Enable", &this->user_enabled)) {
        this->saver->user_disabled = !this->user_enabled;
    }

    ImGui::BeginDisabled(!this->user_enabled);
    if (ImGui::Button("Set Output Folder")) {
        this->output_folder_select = pfd::select_folder("Choose Output Folder");
    }
    if (this->output_folder_select && this->output_folder_select->ready()) {
        this->saver->dir = this->output_folder_select->result();
        this->output_folder_select.reset();
    }
    if (!this->saver->dir.empty()) {
        ImGui::Text("%s", this->saver->dir.c_str());
        ImGui::Text("Saved %ld images", this->saver->file_num);
    }
    ImGui::EndDisabled();

    ImGui::End();
}

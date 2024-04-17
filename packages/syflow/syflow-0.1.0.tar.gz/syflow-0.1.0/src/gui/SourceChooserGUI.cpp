#include "SourceChooserGUI.h"

#include <utility>

#include "imgui.h"
#include "../FileImageSource.h"

using namespace std;

SourceChooserGUI::SourceChooserGUI(std::shared_ptr<Pipeline> pipeline): pipeline(std::move(pipeline)) {}

void SourceChooserGUI::drawImGui() {
    ImGui::Begin("Source Chooser");
    ImGui::BeginDisabled(this->pipeline->running);

    if (ImGui::Button("Test")) {
        vector<string> files;
        for (int i = 0; i < 50; i++) {
            files.push_back("C:\\Users\\user\\Downloads\\piv\\20cm_s_250fps\\png\\CTS_tension_000" + std::to_string(i + 10) + ".png");
        }
        this->pipeline->source = make_shared<FileImageSource>(std::move(files));
    }
    if (ImGui::Button("Open File Source") && !input_file_chooser) {
        input_file_chooser = pfd::open_file("Select Images", ".", {"Image Files", "*.png *.jpg *.jpeg *.bmp *.tif *.tiff"}, pfd::opt::multiselect);
    }
    if (input_file_chooser && input_file_chooser->ready()) {
        // crashes when compiled in Debug mode on Windows, not sure why
        auto files = input_file_chooser->result();
        if (!files.empty()) {
            auto src =  make_shared<FileImageSource>(std::move(files));
            src->preload = true;
            this->pipeline->source = src;
        }
        input_file_chooser.reset();
    }
    for (auto &api : CameraAPI::getAPIs()) {
        if (ImGui::Button(api->getAPIName().c_str())) {
            camera_options = api->getCameras();
            if (camera_options.empty()) {
                pfd::message("Warning", "No cameras found for " + api->getAPIName(), pfd::choice::ok);
            } else {
                chosen_camera_option = 0;
                ImGui::OpenPopup("Choose Camera");
            }
        }
    }
    if (ImGui::BeginPopupModal("Choose Camera")) {
        ImGui::Text("Choose camera");
        ImGui::Separator();

        if (ImGui::BeginCombo("Camera", camera_options[chosen_camera_option]->getName().c_str(), ImGuiComboFlags_WidthFitPreview)) {
            for (size_t i = 0; i < camera_options.size(); i++) {
                bool is_selected = chosen_camera_option == i;
                auto &camera = camera_options[i];
                if (ImGui::Selectable(camera->getName().c_str(), is_selected)) {
                    chosen_camera_option = i;
                }
                if (is_selected) {
                    ImGui::SetItemDefaultFocus();
                }
            }

            ImGui::EndCombo();
        }

        auto &current_choice = camera_options[chosen_camera_option];
        ImGui::Text("%s", current_choice->getDescription().c_str());

        if (ImGui::Button("Cancel", ImVec2(120, 0))) {
            ImGui::CloseCurrentPopup();
        }
        ImGui::SameLine();
        if (ImGui::Button("OK", ImVec2(120, 0))) {
            this->pipeline->source = current_choice;
            ImGui::CloseCurrentPopup();
        }
        ImGui::EndPopup();
    }

    ImGui::EndDisabled();
    ImGui::End();
}

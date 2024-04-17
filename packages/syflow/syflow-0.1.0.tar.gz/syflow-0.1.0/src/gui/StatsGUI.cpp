#include "StatsGUI.h"

#include "imgui.h"

StatsGUI::StatsGUI(std::shared_ptr<Pipeline> pipeline): pipeline(std::move(pipeline)) {}

void StatsGUI::drawImGui() {
    ImGui::Begin("Stats");

    if (this->pipeline->source) {
        ImGui::Text("source(%ld)", this->pipeline->source->images_pushed);
    }
    for (auto& processor : this->pipeline->processors) {
        ImGui::Text("proc(%ld,%ld,%ld)", processor->input_queue.size(), processor->images_popped, processor->images_pushed);
    }
    if (this->pipeline->sink) {
        size_t sink_popped = this->pipeline->sink->images_popped;
        size_t sink_popped_fps = /*sink_popped - last_sink_popped*/0;
        ImGui::Text("sink(%ld,%ld)", this->pipeline->sink->input_queue.size(), sink_popped);
        //last_sink_popped = sink_popped;
    }

    ImGui::Text("Render %.1f FPS", ImGui::GetIO().Framerate);
    ImGui::End();
}
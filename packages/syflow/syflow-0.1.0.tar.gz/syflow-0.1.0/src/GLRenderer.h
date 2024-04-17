#pragma once

#include "Pipeline.h"
#include <memory>
#include <utility>
#include "Shader.h"
#include <glad/glad.h>
#include <cuda_gl_interop.h>
#include <atomic>
#include "OpticalFlowImage.h"
#include "TextureManager.h"
#include "gui/GUIComponent.h"

extern const char* DISPLAY_OPTION_NAMES[];
enum DisplayOption {
    NONE,
    INPUT_IMAGE,
    U,
    V,
    MAX
};

class GLRenderer : public ImageSink, public GUIComponent {
public:
    GLRenderer();
    void drawOpenGL(int width, int height) override;

    bool display_arrows{};
    // DisplayOption enum, but need to use int for ImGui
    int display_option{INPUT_IMAGE};
    float display_range[2] = {-10.0f, 10.0f};
    float arrows_display_scale{1.0f};

    TextureManager image_texture;
    unsigned int image_vbo{}, image_vao{}, image_ebo{};
    // arrows uniforms
    int arrows_width_vectors{}, arrows_block_size{}, arrows_transform_mat{}, arrows_shaft_width{}, arrows_display_scale_uni{}, arrows_max_magnitude{};
    // image uniforms
    int image_transform{}, display_option_uniform{}, display_range_uniform{};
    unsigned int arrows_vbo{}, arrows_vao{};
    cudaGraphicsResource* cuda_arrows_resource = nullptr;
    cudaStream_t streams[2] = { nullptr };
    uint32_t flow_vec_downsample{8};
protected:
    void run_thread() override;
    void on_thread_stop() override;
private:
    void Init();
    void RenderImage(float* screen_transform) const;
    Shader image_shader, arrows_shader;
    std::mutex next_image_mutex;
    std::shared_ptr<OpticalFlowImage> next_image;
    float image_aspect_ratio{1.0f};
    uint32_t last_flow_vec_dims[2]{};
    int last_flow_vec_block_size{0};
    bool initialized = false;
};
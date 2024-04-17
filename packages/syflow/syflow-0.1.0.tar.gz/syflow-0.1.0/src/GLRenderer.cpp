#include "GLRenderer.h"
#include "OpticalFlowUploader.h"
#include "Log.h"
#include "GLUtils.h"

using namespace std;

const char* DISPLAY_OPTION_NAMES[] = {"None", "Input Image", "U", "V"};

GLRenderer::GLRenderer() {
    this->Init();
}

void GLRenderer::Init() {
    if (this->initialized) {
        return;
    }

    Log() << "init renderer";

    float vertices[] = {
            0.0f, 1.0f,
            0.0f, 0.0f,
            1.0f, 0.0f,
            1.0f, 1.0f
    };
    unsigned int indices[] = {
            0, 1, 3, // top left triangle
            1, 2, 3 // bottom right triangle
    };

    glGenVertexArrays(1, &this->image_vao);
    glBindVertexArray(this->image_vao);

    glGenBuffers(1, &this->image_vbo);
    glBindBuffer(GL_ARRAY_BUFFER, this->image_vbo);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glGenBuffers(1, &this->image_ebo);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, this->image_ebo);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    // position attribute
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(float), 0);
    glEnableVertexAttribArray(0);

    this->image_shader.load("image_vertex.glsl", "image_fragment.glsl");
    glUseProgram(this->image_shader.program_id);
    glUniform1i(glGetUniformLocation(this->image_shader.program_id, "texture1"), 0);
    this->display_option_uniform = glGetUniformLocation(this->image_shader.program_id, "display_option");
    this->display_range_uniform = glGetUniformLocation(this->image_shader.program_id, "display_range");
    this->image_transform = glGetUniformLocation(this->image_shader.program_id, "screen_transform");

    // arrows
    glGenVertexArrays(1, &this->arrows_vao);
    glBindVertexArray(this->arrows_vao);

    glGenBuffers(1, &this->arrows_vbo);
    glBindBuffer(GL_ARRAY_BUFFER, this->arrows_vbo);
    glVertexAttribPointer(0, sizeof(float), GL_FLOAT, false, sizeof(Point<float>), nullptr);
    glEnableVertexAttribArray(0);

    this->arrows_shader.load("arrows_vertex.glsl", "arrows_geometry.glsl", "arrows_fragment.glsl");
    this->arrows_width_vectors = glGetUniformLocation(this->arrows_shader.program_id, "width_vectors");
    this->arrows_block_size = glGetUniformLocation(this->arrows_shader.program_id, "block_size");
    this->arrows_transform_mat = glGetUniformLocation(this->arrows_shader.program_id, "pixel_space_to_ndc");
    this->arrows_shaft_width = glGetUniformLocation(this->arrows_shader.program_id, "shaft_width");
    this->arrows_display_scale_uni = glGetUniformLocation(this->arrows_shader.program_id, "display_scale");
    this->arrows_max_magnitude = glGetUniformLocation(this->arrows_shader.program_id, "max_magnitude");

    CheckGLError();

    checkCudaRT(cudaStreamCreate(&this->streams[0]));
    checkCudaRT(cudaStreamCreate(&this->streams[1]));

    this->initialized = true;
}

// multiply column-order 3x3 matrix
static void multiply_mat3(float a[][3], float b[][3], float out[][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            float sum = 0.0;
            for (int k = 0; k < 3; k++) {
                sum += a[k][i] * b[j][k];
            }
            out[j][i] = sum;
        }
    }
}

void GLRenderer::drawOpenGL(int width, int height) {
    std::shared_ptr<OpticalFlowImage> new_image;
    {
        std::unique_lock lock(this->next_image_mutex);
        new_image = std::move(this->next_image);
    }
    if (new_image) {
        this->image_aspect_ratio = (float)new_image->gpu_image_nv->getWidth() / (float)new_image->gpu_image_nv->getHeight();
    }

    // transform [0, 1] to NDC [-1, 1] including black bar padding to preserve aspect ratio
    // opengl uses column-major matrices so it looks transposed
    float screen_transform[3][3] = {
            {2.0f, 0.0f, 0.0f},
            {0.0f, 2.0f, 0.0f},
            {-1.0f, -1.0f, 1.0f}
    };

    float screen_aspect_ratio = (float)width / (float)height;

    if (screen_aspect_ratio > this->image_aspect_ratio) {
        // padding on left/right
        float x_shrink_factor = this->image_aspect_ratio / screen_aspect_ratio;
        screen_transform[0][0] *= x_shrink_factor;
        screen_transform[2][0] *= x_shrink_factor;
    }
    else {
        // padding on top/bottom
        float y_shrink_factor = screen_aspect_ratio / this->image_aspect_ratio;
        screen_transform[1][1] *= y_shrink_factor;
        screen_transform[2][1] *= y_shrink_factor;
    }

    switch (this->display_option) {
        case INPUT_IMAGE: {
            if (new_image) {
                new_image->GLUploadSourceImage(*this);
            }
            this->RenderImage((float*) screen_transform);
            break;
        }
        case U:
        case V: {
            if (new_image) {
                auto opt_flow_img = dynamic_cast<OpticalFlowImage*>(new_image.get());
                if (opt_flow_img) {
                    opt_flow_img->GLUploadVectorsTexture(*this);
                }
            }
            this->RenderImage((float*) screen_transform);
            break;
        }
        case NONE:
        default:
            break;
    }

    if (this->display_arrows) {
        if (new_image && new_image->float_vecs) {
            new_image->GLUploadVectorsVAO(*this);
            this->last_flow_vec_dims[0] = new_image->float_vecs->width / this->flow_vec_downsample;
            this->last_flow_vec_dims[1] = new_image->float_vecs->height / this->flow_vec_downsample;
            this->last_flow_vec_block_size = new_image->block_size * this->flow_vec_downsample;
        }

        // transform [0, width_pixels] x [0, height_pixels] -> [0, 1] x [0, 1]
        float pixel_space_to_image_space[3][3] = {
                { 1.0f / ((float)this->last_flow_vec_dims[0] * (float)this->last_flow_vec_block_size), 0.0, 0.0 },
                { 0.0, 1.0f / ((float)this->last_flow_vec_dims[1] * (float)this->last_flow_vec_block_size), 0.0 },
                { 0.0, 0.0, 1.0 }
        };

        float pixel_space_to_ndc_backward[3][3];
        multiply_mat3(screen_transform, pixel_space_to_image_space, pixel_space_to_ndc_backward);

        float flip_y[3][3] = {
                { 1.0, 0.0, 0.0 },
                { 0.0, -1.0, 0.0 },
                { 0.0, 0.0, 1.0 }
        };
        float pixel_space_to_ndc[3][3];
        multiply_mat3(flip_y, pixel_space_to_ndc_backward, pixel_space_to_ndc);

        glUseProgram(this->arrows_shader.program_id);
        glUniform1ui(this->arrows_width_vectors, this->last_flow_vec_dims[0]);
        glUniform1ui(this->arrows_block_size, this->last_flow_vec_block_size);
        auto shaft_width = static_cast<float>(this->last_flow_vec_block_size) / 5.0f;
        glUniform1f(this->arrows_shaft_width, shaft_width);
        glUniform1f(this->arrows_display_scale_uni, this->arrows_display_scale);
        glUniform1f(this->arrows_max_magnitude, max(-this->display_range[0], this->display_range[1]));
        glUniformMatrix3fv(this->arrows_transform_mat, 1, false, (float*)pixel_space_to_ndc);
        glBindVertexArray(this->arrows_vao);
        glDrawArrays(GL_POINTS, 0, (GLsizei) (this->last_flow_vec_dims[0] * this->last_flow_vec_dims[1]));
    }

    CheckGLError();
}

void GLRenderer::run_thread()
{
    while (this->keep_running.load()) {
        auto maybe_next_image = this->pop_blocking();
        if (!maybe_next_image) break;

        {
            std::unique_lock lock(this->next_image_mutex);
            this->next_image = maybe_next_image;
        }
    }
}

void GLRenderer::on_thread_stop()
{
    if (this->cuda_arrows_resource) {
        checkCudaRT(cudaGraphicsUnregisterResource(this->cuda_arrows_resource));
    }

    {
        std::unique_lock lock(this->next_image_mutex);
        this->next_image.reset();
    }
}

void GLRenderer::RenderImage(float* screen_transform) const {
    glUseProgram(this->image_shader.program_id);
    glBindTextureUnit(0, this->image_texture.texture_id);
    glUniform1ui(this->display_option_uniform, (unsigned int) this->display_option);
    if (this->display_option == DisplayOption::U || this->display_option == DisplayOption::V) {
        glUniform2fv(this->display_range_uniform, 1, this->display_range);
    }

    glUniformMatrix3fv(this->image_transform, 1, false, screen_transform);

    glBindVertexArray(this->image_vao);
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, nullptr);
}
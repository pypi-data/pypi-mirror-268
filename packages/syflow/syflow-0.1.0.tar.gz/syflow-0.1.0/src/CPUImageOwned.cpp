#include "CPUImageOwned.h"
#include <glad/glad.h>
#include "GLUtils.h"
#include "CudaImage.h"
#include "GLRenderer.h"

template <typename T>
static void GLUploadSourceImage_specific(const CPUImageOwned<T> &image, GLRenderer &renderer, int internal_format, int upload_format, int upload_element_type) {
    renderer.image_texture.UpdateParams(image.width, image.height, internal_format);
    glTextureSubImage2D(renderer.image_texture.texture_id, 0, 0, 0, image.width, image.height, upload_format, upload_element_type, image.data);
    CheckGLError();
}

template<> void CPUImageOwned<uint8_t>::GLUploadSourceImage(GLRenderer &renderer) {
    GLUploadSourceImage_specific(*this, renderer, GL_R8, GL_RED, GL_UNSIGNED_BYTE);
}

template<> void CPUImageOwned<S105Vector>::GLUploadSourceImage(GLRenderer &renderer) {
    GLUploadSourceImage_specific(*this, renderer, GL_RG16_SNORM, GL_RG, GL_SHORT);
}

template<> void CPUImageOwned<Point<float>>::GLUploadSourceImage(GLRenderer &renderer) {
    GLUploadSourceImage_specific(*this, renderer, GL_RG32F, GL_RG, GL_FLOAT);
}
#include "GLUtils.h"

#include <glad/glad.h>

void internal_checkCudaRT(cudaError result, char const* const func, const char* const file, int const line) {
    if (result) {
        Log() << "CUDA error at " << file << ":" << line << " code = " << static_cast<unsigned int>(result) << "(" << cudaGetErrorName(result) << ") \"" << func << "\"";
        exit(EXIT_FAILURE);
    }
}

void internal_checkCudaDriver(cudaError_enum result, char const* const func, const char* const file,
                              int const line) {
    if (result) {
        const char *error_name;
        cuGetErrorName(result, &error_name);
        Log() << "CUDA error at " << file << ":" << line << " code = " << static_cast<unsigned int>(result) << "(" << error_name << ") \"" << func << "\"";
        exit(EXIT_FAILURE);
    }
}

void internal_CheckGLError(char const* const file, int line) {
    bool has_error = false;
    for (auto error = glGetError(); error != GL_NO_ERROR; error = glGetError()) {
        Log() << "OpenGL error " << error << " at " << file << ":" << line;
        has_error = true;
    }
    if (has_error) {
        exit(EXIT_FAILURE);
    }
}
#include "TextureManager.h"

#include "GLUtils.h"

void TextureManager::UpdateParams(int width, int height, int gl_internal_format) {
    if (width == current_width && height == current_height && gl_internal_format == current_internal_format) {
        // already good
        return;
    }
    Log() << "make texture width " << width << " height " << height << " internal format " << gl_internal_format;
    this->current_width = width;
    this->current_height = height;
    this->current_internal_format = gl_internal_format;
    if (this->texture_id != 0) {
        glDeleteTextures(1, &this->texture_id);
    }
    glCreateTextures(GL_TEXTURE_2D, 1, &this->texture_id);
    glTextureParameteri(this->texture_id, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTextureParameteri(this->texture_id, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTextureParameteri(this->texture_id, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTextureParameteri(this->texture_id, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTextureStorage2D(this->texture_id, 1, gl_internal_format, width, height);

    if (this->cuda_resource) {
        checkCudaRT(cudaGraphicsUnregisterResource(this->cuda_resource));
        this->cuda_resource = nullptr;
    }
    Log() << "register cuda resource";
    cudaError_t status = cudaGraphicsGLRegisterImage(&this->cuda_resource, this->texture_id, GL_TEXTURE_2D, cudaGraphicsRegisterFlagsWriteDiscard);
    if (status == cudaSuccess) {
        Log() << "cuda register success";
    } else {
        // running renderer on a different GPU
        // we will download image from nvidia GPU -> cpu -> other GPU
        Log() << "error registering cuda_tex_resource: " << cudaGetErrorName(status) << ", will download images to CPU before displaying";
    }

    CheckGLError();
}

void TextureManager::CopyFromDevicePtr(NvOFBufferCudaDevicePtr *cu_device_ptr_obj, cudaStream_t stream) {
    // rendering on same GPU that does optical flow processing
    // therefore, we don't need to download image to CPU first
    // based off of processImage() in postProcessGL cuda sample

    // get a cudaArray* for the OpenGL texture
    cudaArray *texture_ptr;
    checkCudaRT(cudaGraphicsMapResources(1, &this->cuda_resource, stream));
    checkCudaRT(cudaGraphicsSubResourceGetMappedArray(&texture_ptr, this->cuda_resource, 0, 0));

    // copy the image data

    CUdeviceptr src = cu_device_ptr_obj->getCudaDevicePtr();
    checkCudaRT(cudaMemcpy2DToArrayAsync(texture_ptr, 0, 0, (void *) src,
                                         cu_device_ptr_obj->getStrideInfo().strideInfo->strideXInBytes,
                                             cu_device_ptr_obj->getWidth() * cu_device_ptr_obj->getElementSize(),
                                         cu_device_ptr_obj->getHeight(), cudaMemcpyDeviceToDevice,
                                         stream));

    // unused code, if copying from CUarray instead
    //NvOFBufferCudaArray* cu_array_buf = dynamic_cast<NvOFBufferCudaArray*>(opt_flow_image->gpu_image.get());
    //CUarray src = cu_array_buf->getCudaArray();
    //checkCudaErrors(cudaMemcpy2DArrayToArray(texture_ptr, 0, 0, (cudaArray*) src, 0, 0, opt_flow_image->gpu_image->getWidth(), opt_flow_image->gpu_image->getHeight()));

    checkCudaRT(cudaGraphicsUnmapResources(1, &this->cuda_resource, stream));

    checkCudaRT(cudaStreamSynchronize(stream));
}

TextureManager::~TextureManager() {
    if (this->texture_id) {
        glDeleteTextures(1, &this->texture_id);
    }
}

#include "Log.h"
#include <cuda.h>
#include <cuda_runtime.h>

void internal_CheckGLError(char const* file, int line);

#define CheckGLError() internal_CheckGLError(__FILE__, __LINE__)

// error checking based off of postProcessGL.cu in nvidia cuda samples
void internal_checkCudaRT(cudaError result, char const* func, const char* file, int line);

// This will output the proper CUDA error strings in the event
// that a CUDA host call returns an error. For cuda runtime API only.
#define checkCudaRT(val) internal_checkCudaRT((val), #val, __FILE__, __LINE__)

void internal_checkCudaDriver(cudaError_enum result, char const* func, const char* file, int line);
// For cuda driver API.
#define checkCudaDrv(val) internal_checkCudaDriver(val, #val, __FILE__, __LINE__)
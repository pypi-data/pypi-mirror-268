/*
* Copyright (c) 2018-2023 NVIDIA Corporation
*
* Permission is hereby granted, free of charge, to any person
* obtaining a copy of this software and associated documentation
* files (the "Software"), to deal in the Software without
* restriction, including without limitation the rights to use,
* copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the software, and to permit persons to whom the
* software is furnished to do so, subject to the following
* conditions:
*
* The above copyright notice and this permission notice shall be
* included in all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
* OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
* NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
* HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
* WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
* OTHER DEALINGS IN THE SOFTWARE.
*/


#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <iomanip>
#include "NvOFUtils.h"

#define UNKNOWN_FLOW_THRESH 1e9

#if !defined(M_PI)
#define M_PI 3.14159265358979f
#endif

#if defined(ENABLE_RAW_NVOF_OUTPUT)
void NvOFFileWriterStereo::WriteRawNvFlowVectors(const void* flowVectors, const std::string filename)
{
    std::ofstream fpOut(filename + std::string("_nvdisp.bin"), std::ios::out | std::ios::binary);
    fpOut.write((const char*)flowVectors, sizeof(NV_OF_STEREO_DISPARITY) * m_width * m_height);
    fpOut.close();
}
#endif

NvOFUtils::NvOFUtils(NV_OF_MODE eMode)
    : m_eMode(eMode)
{
}
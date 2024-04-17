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


#pragma once
#include <stdint.h>
#include <memory>
#include <math.h>
#include <string>
#include <array>
#include <chrono>
#define NOMINMAX
#include "nvOpticalFlowCommon.h"

class NvOFBuffer;
class NvOFUtils
{
public:
    NvOFUtils(NV_OF_MODE eMode);
    virtual ~NvOFUtils() {}
    virtual void Upsample(NvOFBuffer *srcBuffer, NvOFBuffer *dstBuffer, uint32_t nScaleFactor) = 0;
protected:
    NV_OF_MODE m_eMode;
};

/*
 * NvOFStopWatch class provide methods for starting and stopping timer.
 */
class NvOFStopWatch
{
public:
    NvOFStopWatch(bool start = false)
    {
        if (start)
            Start();
    }

    void Start()
    {
        t0 = std::chrono::high_resolution_clock::now();

    }

    double ElapsedTime()
    {
        double d = std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now().time_since_epoch() - t0.time_since_epoch()).count() / 1.0e9;
        return d;
    }

    double Stop()
    {
        double d = std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now().time_since_epoch() - t0.time_since_epoch()).count() / 1.0e9;
        return d;
    }
private:
    std::chrono::high_resolution_clock::time_point t0;
};


#pragma once

#include "Pipeline.h"
#include <linux/videodev2.h>

class V4L2Source : public ImageSource {
public:
    void run_thread() override;
protected:
    void on_thread_stop() override;
private:
    void init_device();
    void start_capturing();
    void main_loop();
    void stop_capturing();


    int fd;
    struct {
        void *start;
        size_t length;
    } *buffers;
    unsigned int num_buffers;
    struct v4l2_requestbuffers reqbuf = {0};

    void process_image(const void *pBuffer);

    int read_frame();

    void init_mmap();
};
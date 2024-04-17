#pragma clang diagnostic push
#pragma ide diagnostic ignored "readability-make-member-function-const"
#include "V4L2Source.h"

// based off of https://github.com/kmdouglass/v4l2-examples/blob/master/example-5/example-5.c

#include <cassert>
#include <cerrno>
#include <fcntl.h>
#include <linux/videodev2.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sys/mman.h>
#include <sys/time.h>
#include <sys/ioctl.h>
#include <unistd.h>

static const char DEVICE[] = "/dev/video2";

/**
 * Wrapper around ioctl calls.
 */
static int xioctl(int fd, int request, void *arg) {
    int r;

    do {
        r = ioctl(fd, request, arg);
    } while (-1 == r && EINTR == errno);

    return r;
}

void V4L2Source::init_mmap() {
    reqbuf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    reqbuf.memory = V4L2_MEMORY_MMAP;
    reqbuf.count = 5;
    if (-1 == xioctl(fd, VIDIOC_REQBUFS, &reqbuf)) {
        perror("VIDIOC_REQBUFS");
        exit(errno);
    }

    if (reqbuf.count < 2){
        printf("Not enough buffer memory\n");
        exit(EXIT_FAILURE);
    }

    buffers = (decltype(buffers)) calloc(reqbuf.count, sizeof(*buffers));
    assert(buffers != nullptr);

    num_buffers = reqbuf.count;

    // Create the buffer memory maps
    struct v4l2_buffer buffer{};
    for (unsigned int i = 0; i < reqbuf.count; i++) {
        memset(&buffer, 0, sizeof(buffer));
        buffer.type = reqbuf.type;
        buffer.memory = V4L2_MEMORY_MMAP;
        buffer.index = i;

        // Note: VIDIOC_QUERYBUF, not VIDIOC_QBUF, is used here!
        if (-1 == xioctl(fd, VIDIOC_QUERYBUF, &buffer)) {
            perror("VIDIOC_QUERYBUF");
            exit(errno);
        }

        buffers[i].length = buffer.length;
        buffers[i].start = mmap(
                nullptr,
                buffer.length,
                PROT_READ | PROT_WRITE,
                MAP_SHARED,
                fd,
                buffer.m.offset
        );

        if (MAP_FAILED == buffers[i].start) {
            perror("mmap");
            exit(errno);
        }
    }
}

void V4L2Source::init_device() {
    struct v4l2_fmtdesc fmtdesc = {0};
    fmtdesc.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    // Get the format with the largest index and use it
    while(0 == xioctl(fd, VIDIOC_ENUM_FMT, &fmtdesc)) {
        fmtdesc.index++;
    }
    printf("\nUsing format: %s\n", fmtdesc.description);

    struct v4l2_format fmt = {0};
    fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    fmt.fmt.pix.width = 640;
    fmt.fmt.pix.height = 480;
    fmt.fmt.pix.pixelformat = fmtdesc.pixelformat;
    fmt.fmt.pix.field = V4L2_FIELD_NONE;

    if (-1 == xioctl(fd, VIDIOC_S_FMT, &fmt)) {
        perror("VIDIOC_S_FMT");
        exit(errno);
    }

    char format_code[5];
    strncpy(format_code, (char*)&fmt.fmt.pix.pixelformat, 5);
    printf(
            "Set format:\n"
            " Width: %d\n"
            " Height: %d\n"
            " Pixel format: %s\n"
            " Field: %d\n\n",
            fmt.fmt.pix.width,
            fmt.fmt.pix.height,
            format_code,
            fmt.fmt.pix.field
    );

    init_mmap();
}

void V4L2Source::start_capturing() {
    enum v4l2_buf_type type;

    struct v4l2_buffer buffer{};
    for (unsigned int i = 0; i < num_buffers; i++) {
        /* Note that we set bytesused = 0, which will set it to the buffer length
         * See
         * - https://www.linuxtv.org/downloads/v4l-dvb-apis-new/uapi/v4l/vidioc-qbuf.html?highlight=vidioc_qbuf#description
         * - https://www.linuxtv.org/downloads/v4l-dvb-apis-new/uapi/v4l/buffer.html#c.v4l2_buffer
         */
        memset(&buffer, 0, sizeof(buffer));
        buffer.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
        buffer.memory = V4L2_MEMORY_MMAP;
        buffer.index = i;

        // Enqueue the buffer with VIDIOC_QBUF
        if (-1 == xioctl(fd, VIDIOC_QBUF, &buffer)) {
            perror("VIDIOC_QBUF");
            exit(errno);
        }
    }

    type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    if (-1 == xioctl(fd, VIDIOC_STREAMON, &type)) {
        perror("VIDIOC_STREAMON");
        exit(errno);
    }

}

void V4L2Source::stop_capturing() {
    enum v4l2_buf_type type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    if (-1 == xioctl(fd, VIDIOC_STREAMOFF, &type)) {
        perror("VIDIOC_STREAMOFF");
        exit(errno);
    }
}

/**
 * Draws a dot on the screen.
 *
 * Normally, the buffer would be processed here.
 */
void V4L2Source::process_image(const void * pBuffer) {
    int width = 576;
    int height = 360;
    void* copy = malloc(width * height);
    memcpy(copy, pBuffer, width * height);
    auto opt_flow_img = std::make_shared<OpticalFlowImage>();
    opt_flow_img->cpu_image = std::make_shared<CPUImageOwned<uint8_t>>(width, height, copy);
    this->push_nonblocking(opt_flow_img);
}

/**
 * Readout a frame from the buffers.
 */
int V4L2Source::read_frame() {
    struct v4l2_buffer buffer{};
    memset(&buffer, 0, sizeof(buffer));
    buffer.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    buffer.memory = V4L2_MEMORY_MMAP;

    // Dequeue a buffer
    if (-1 == xioctl(fd, VIDIOC_DQBUF, &buffer)) {
        switch(errno) {
            case EAGAIN:
                // No buffer in the outgoing queue
                return 0;
            case EIO:
                // fall through
            default:
                perror("VIDIOC_DQBUF");
                exit(errno);
        }
    }

    assert(buffer.index < num_buffers);

    process_image(buffers[buffer.index].start);

    // Enqueue the buffer again
    if (-1 == xioctl(fd, VIDIOC_QBUF, &buffer)) {
        perror("VIDIOC_QBUF");
        exit(errno);
    }

    return 1;
}

/**
 * Poll the device until it is ready for reading.
 *
 * See https://www.gnu.org/software/libc/manual/html_node/Waiting-for-I_002fO.html
 */
void V4L2Source::main_loop() {
    while(this->keep_running) {
        fd_set fds;
        struct timeval tv{};
        int r;
        for (;;) {
            // Clear the set of file descriptors to monitor, then add the fd for our device
            FD_ZERO(&fds);
            FD_SET(fd, &fds);

            // Set the timeout
            tv.tv_sec = 2;
            tv.tv_usec = 0;

            /**
             * Arguments are
             * - number of file descriptors
             * - set of read fds
             * - set of write fds
             * - set of except fds
             * - timeval struct
             *
             * According to the man page for select, "nfds should be set to the highest-numbered file
             * descriptor in any of the three sets, plus 1."
             */
            r = select(fd + 1, &fds, nullptr, nullptr, &tv);

            if (-1 == r) {
                if (EINTR == errno)
                    continue;

                perror("select");
                exit(errno);
            }

            if (0 == r) {
                fprintf (stderr, "select timeout\n");
                exit(EXIT_FAILURE);
            }

            if (read_frame())
                // Go to next iterartion of fhe while loop; 0 means no frame is ready in the outgoing queue.
                break;
        }
    }
}

void V4L2Source::run_thread() {
    // Open the device file
    fd = open(DEVICE, O_RDWR);
    if (fd < 0) {
        perror(DEVICE);
        return;
    }

    init_device();
    start_capturing();
    main_loop();
}

void V4L2Source::on_thread_stop() {
    stop_capturing();

    // Cleanup
    for (unsigned int i = 0; i < reqbuf.count; i++)
        munmap(buffers[i].start, buffers[i].length);
    free(buffers);
    close(fd);
}

#pragma clang diagnostic pop
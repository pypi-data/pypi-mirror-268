#pragma once

#include "ThreadSafeQueue.h"
#include "OpticalFlowImage.h"
#include <atomic>
#include <memory>
#include <vector>
#include <string>
#include <thread>
#include <cuda.h>

typedef ThreadSafeQueue<std::shared_ptr<OpticalFlowImage>> ImageQueue;

// background loop runner
class BgRunnerLoop {
public:
	virtual void run();
	void stop();
	virtual ~BgRunnerLoop();
protected:
	// if the loop should keep running
	std::atomic<bool> keep_running{false};
	// function to run in background thread
	virtual void run_thread() = 0;
	// called before waiting for background thread to stop
	virtual void prepare_to_stop() {};
	// function to run after background thread finishes
	virtual void on_thread_stop() {};

	std::thread bg_thread;
};

class ImageSource : public virtual BgRunnerLoop {
public:
	~ImageSource() override = default;
	// ImageSource does not own the queue
	ImageQueue* output_queue = nullptr;
	// images pushed, including non-blocking pushes that failed (and were then dropped)
	size_t images_pushed = 0;
	void prepare_to_stop() override;
	bool push_nonblocking(std::shared_ptr<OpticalFlowImage> image);
	void push_blocking(std::shared_ptr<OpticalFlowImage> image);
};

class ImageSink : public virtual BgRunnerLoop {
public:
	static const size_t QUEUE_SIZE = 10;
	~ImageSink() override = default;
	// ImageSink owns the queue
	ImageQueue input_queue{ QUEUE_SIZE };
	size_t images_popped = 0;
protected:
	void prepare_to_stop() override;
	// return the head of the queue, or wait for the next image.
	// can return nullptr, in which case the thread should shut down
	std::shared_ptr<OpticalFlowImage> pop_blocking();
};

// ImageProcessor takes input, processes, and produces output
class ImageProcessor : public ImageSource, public ImageSink {
public:
    void run_thread() override;

    // optional hook to run when the pipeline is started
    virtual void on_thread_start();
    virtual void process_image(const std::shared_ptr<OpticalFlowImage> &image) = 0;
    // disable this processor, only has an effect when starting the pipeline
    virtual bool disabled();
	void prepare_to_stop() override;
};

class Pipeline {
private:
    std::vector<std::shared_ptr<ImageProcessor>> GetEnabledProcessors();
public:
    Pipeline();
    void Start();
	void Stop();

    bool running = false;

	// first source
    std::shared_ptr<ImageSource> source;
	// intermediate processors
	std::vector<std::shared_ptr<ImageProcessor>> processors;
	// final sink
    std::shared_ptr<ImageSink> sink;
};
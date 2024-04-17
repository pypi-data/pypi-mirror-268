#include "Pipeline.h"
#include "Log.h"
#include "FileImageSource.h"
#include "vendor/nvof/NvOFCuda.h"

using namespace std;

/* BGRunnerLoop */

void BgRunnerLoop::run() {
	this->keep_running.store(true);
	this->bg_thread = std::thread{ &BgRunnerLoop::run_thread, this };
}

void BgRunnerLoop::stop() {
	bool expected = true;
	if (this->keep_running.compare_exchange_strong(expected, false)) {
		this->prepare_to_stop();
		this->bg_thread.join();
        this->on_thread_stop();
	}
}

BgRunnerLoop::~BgRunnerLoop() {
	if (this->keep_running.load()) {
		Log() << "background runner destructed without first stopping";
	}
}

/* ImageSource */

void ImageSource::prepare_to_stop() {
	// flush is required because the thread could be stuck on push_blocking()
	this->output_queue->clear();
}

bool ImageSource::push_nonblocking(std::shared_ptr<OpticalFlowImage> image)
{
	this->images_pushed++;
	return this->output_queue->try_push(std::move(image));
}

void ImageSource::push_blocking(std::shared_ptr<OpticalFlowImage> image)
{
	this->images_pushed++;
	this->output_queue->push(std::move(image));
}

/* ImageSink */

void ImageSink::prepare_to_stop() {
	// can be stuck on pop_blocking, so send null image
	Log() << "imagesink push null";
	std::shared_ptr<OpticalFlowImage> null_image;
	this->input_queue.try_push(std::move(null_image));
}

std::shared_ptr<OpticalFlowImage> ImageSink::pop_blocking() {
	std::shared_ptr<OpticalFlowImage> image;
	this->input_queue.pop(image);
	this->images_popped++;
	return image;
}

/* ImageProcessor */

void ImageProcessor::prepare_to_stop()
{
	ImageSource::prepare_to_stop();
	ImageSink::prepare_to_stop();
}

bool ImageProcessor::disabled() {
    return false;
}

void ImageProcessor::run_thread() {
    while (this->keep_running.load()) {
        auto img = this->pop_blocking();
        if (!img) break;

        this->process_image(img);
        this->push_blocking(img);
    }
}

void ImageProcessor::on_thread_start() {}

/* Pipeline */

Pipeline::Pipeline() = default;

void Pipeline::Start() {
    if (this->running) {
        throw std::invalid_argument("start when already running");
    }
    if (!this->source) {
        throw std::invalid_argument("missing source");
    }
    if (!this->sink) {
        throw std::invalid_argument("missing sink");
    }
    this->running = true;

    // connect source to first processor
    auto enabled_processors = this->GetEnabledProcessors();
    if (enabled_processors.empty()) {
        this->source->output_queue = &this->sink->input_queue;
    } else {
        this->source->output_queue = &enabled_processors[0]->input_queue;
    }

    if (!enabled_processors.empty()) {
        for (size_t i = 0; i < enabled_processors.size() - 1; i++) {
            enabled_processors[i]->output_queue = &enabled_processors[i + 1]->input_queue;
        }
    }

    if (!enabled_processors.empty()) {
        enabled_processors[enabled_processors.size() - 1]->output_queue = &this->sink->input_queue;
    }

    Log() << "run pipeline";
    this->source->run();
    for (auto &processor: enabled_processors) {
        processor->run();
    }
    this->sink->run();
}

void Pipeline::Stop() {
    if (!this->running) {
        throw std::invalid_argument("stop when not running");
    }
	if (this->source) {
		this->source->stop();
	}
    Log() << "stop pipeline";
    this->source->stop();
	for (auto& processor : this->processors) {
		processor->stop();
        processor->input_queue.clear();
	}
    this->sink->stop();
    this->sink->input_queue.clear();

    this->running = false;
}

std::vector<std::shared_ptr<ImageProcessor>> Pipeline::GetEnabledProcessors() {
    std::vector<std::shared_ptr<ImageProcessor>> enabled;
    for (auto &proc : this->processors) {
        if (!proc->disabled()) {
            enabled.push_back(proc);
        }
    }
    return enabled;
}

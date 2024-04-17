#pragma once

#include <queue>
#include <mutex>
#include <condition_variable>
#include <cassert>

// simple locking queue with bounded capacity
// if more features needed could use something like https://github.com/cameron314/concurrentqueue/blob/master/blockingconcurrentqueue.h
template<typename T>
class ThreadSafeQueue {
public:
	ThreadSafeQueue(size_t max_size) {
		this->max_size = max_size;
	}
    // true if value popped
	bool try_pop(T& val) {
		{
			std::unique_lock lock(this->mutex);
			if (this->queue.empty()) {
				return false;
			}
			else {
				val = std::move(this->queue.front());
				this->queue.pop();
			}
		}
		this->not_full_cond.notify_one();
		return true;
	}
	void pop(T& val) {
		{
			std::unique_lock lock(this->mutex);
			while (this->queue.empty()) {
				this->not_empty_cond.wait(lock);
			}
			val = std::move(this->queue.front());
			this->queue.pop();
		}
		this->not_full_cond.notify_one();
	}
	bool try_push(T&& val) {
		{
			std::unique_lock lock(mutex);
			if (queue.size() == max_size) {
				return false;
			}
			else {
				this->queue.push(std::move(val));
			}
		}
		this->not_empty_cond.notify_one();
		return true;
	}
	void push(T&& val) {
		{
			std::unique_lock lock(mutex);
			while (queue.size() == max_size) {
				this->not_full_cond.wait(lock);
			}
			this->queue.push(std::move(val));
		}
		this->not_empty_cond.notify_one();
	}
	void clear() {
		std::unique_lock lock(mutex);
		this->queue = {};
		this->not_full_cond.notify_one();
	}
	size_t size() {
		std::unique_lock lock(mutex);
		return this->queue.size();
	}

    ThreadSafeQueue(const ThreadSafeQueue&) = delete;
    ThreadSafeQueue& operator=(const ThreadSafeQueue&) = delete;
private:
	std::queue<T> queue;
	size_t max_size{};
	std::mutex mutex;
	std::condition_variable not_empty_cond;
	std::condition_variable not_full_cond;
};
#pragma once

#include <queue>

template <typename T>
class RollingAverage {
public:
    RollingAverage(size_t max_samples = 25): max_samples(max_samples) {}
    size_t max_samples;
    void push(T t) {
        this->samples.push(std::move(t));
    }
private:
    std::queue<T> samples;
};
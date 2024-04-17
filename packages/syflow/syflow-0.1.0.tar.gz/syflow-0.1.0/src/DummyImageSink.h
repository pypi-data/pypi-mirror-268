#pragma once

#include "Pipeline.h"

class DummyImageSink: public ImageSink {
    void run_thread() override;
};

#pragma once

#include "Pipeline.h"

class FileImageSource : public ImageSource {
public:
	static std::shared_ptr<CPUImageOwned<uint8_t>> load_image(const std::string &filename);
	FileImageSource(std::vector<std::string> &&filenames);
	void run_thread() override;

    bool preload = false;
private:
	std::vector<std::string> filenames;
	size_t next;
};
#include "FileImageSource.h"
#define STB_IMAGE_IMPLEMENTATION
#include "vendor/stb_image.h"
#include "Log.h"

using namespace std;

FileImageSource::FileImageSource(vector<string> &&_filenames): filenames(_filenames), next(0) {}

shared_ptr<CPUImageOwned<uint8_t>> FileImageSource::load_image(const string& filename) {
	int x, y, comp;
	uint8_t* data = stbi_load(filename.c_str(), &x, &y, &comp, 1);
	if (data == nullptr) {
		throw invalid_argument(stbi_failure_reason());
	} else if (comp == 1) {
        return make_shared<CPUImageOwned<uint8_t>>(x, y, data);
    }
	else {
        throw std::invalid_argument("invalid number of channels: " + std::to_string(comp));
	}
}

void FileImageSource::run_thread() {
	if (this->preload) {
		vector<shared_ptr<CPUImageOwned<uint8_t>>> images;
		for (auto& filename : this->filenames) {
			images.push_back(FileImageSource::load_image(filename));
		}
		while (this->keep_running.load()) {
            auto opt_flow_img = std::make_shared<OpticalFlowImage>();
            opt_flow_img->cpu_image = images[this->next];
			this->push_blocking(opt_flow_img);
			this->next = (this->next + 1) % this->filenames.size();
		}
	}
	else {
		while (this->keep_running.load()) {
			string filename = this->filenames[this->next];
            auto opt_flow_img = std::make_shared<OpticalFlowImage>();
            opt_flow_img->cpu_image = FileImageSource::load_image(filename);
			this->push_blocking(opt_flow_img);
			this->next = (this->next + 1) % this->filenames.size();
		}
	}
}
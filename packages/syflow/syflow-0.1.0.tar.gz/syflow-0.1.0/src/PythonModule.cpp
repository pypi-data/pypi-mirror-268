#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <optional>
#include "Pipeline.h"
#include "OpticalFlowUploader.h"
#include "OpticalFlowExecutor.h"
#include "DummyImageSink.h"
#include "FileImageSource.h"
#include "ThreadSafeQueue.h"
#include "GLUtils.h"

#include "Log.h"
#include "CameraAPI.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;
using namespace pybind11::literals;

template<typename T>
static void declare_cpu_image_owned(py::module &m, const char *name) {
    py::class_<CPUImageOwned<T>, std::shared_ptr<CPUImageOwned<T>>>(m, name)
            .def_readonly("width", &CPUImageOwned<T>::width)
            .def_readonly("height", &CPUImageOwned<T>::height);
}

// `channels` is the number of components inside each T, which is used to construct numba array for Python API binding
template<typename T>
static void declare_cuda_image_owned(py::module &m, const char *name, uint32_t channels, const char *numpy_typestr) {
    using Class = CudaImageOwned<T>;
    auto get_shape = [channels](Class &cuda_mem) {
        return py::make_tuple(cuda_mem.height, cuda_mem.width, channels);
    };
    auto get_strides = [channels](Class &cuda_mem) {
        return py::make_tuple(cuda_mem.pitch, sizeof(T), sizeof(T) / channels);
    };
    py::class_<Class, std::shared_ptr<Class>>(m, name)
        .def_property_readonly("shape", get_shape)
        .def_property_readonly("strides", get_strides)
        .def_readonly("device_ptr", &Class::device_ptr)
        .def_property_readonly("__cuda_array_interface__", [get_shape, get_strides, numpy_typestr](Class &cuda_mem) {
            return py::dict("shape"_a=get_shape(cuda_mem),
                            "typestr"_a=numpy_typestr,
                            "data"_a=py::make_tuple(reinterpret_cast<uintptr_t>(cuda_mem.device_ptr), false),
                            "version"_a=3,
                            "strides"_a=get_strides(cuda_mem));
        });
}

template<typename T>
static void declare_cuda_image_ref(py::module &m, const char *name, uint32_t channels, const char *numpy_typestr) {
    using Class = CudaImageRef<T>;
    auto get_shape = [channels](Class &cuda_mem) {
        Log() << "get shape " << channels << "," << cuda_mem.width << "," << cuda_mem.width;
        return py::make_tuple(cuda_mem.height, cuda_mem.width, channels);
    };
    auto get_strides = [channels](Class &cuda_mem) {
        Log() << "get strides " << channels << "," << cuda_mem.pitch;
        return py::make_tuple(cuda_mem.pitch, sizeof(T), sizeof(T) / channels);
    };
    py::class_<Class>(m, name)
            .def_property_readonly("shape", get_shape)
            .def_property_readonly("strides", get_strides)
            .def_readonly("device_ptr", &Class::device_ptr)
            .def_property_readonly("__cuda_array_interface__", [get_shape, get_strides, numpy_typestr](Class &cuda_mem) {
                return py::dict("shape"_a=get_shape(cuda_mem),
                                "typestr"_a=numpy_typestr,
                                "data"_a=py::make_tuple(reinterpret_cast<uintptr_t>(cuda_mem.device_ptr), false),
                                "version"_a=3,
                                "strides"_a=get_strides(cuda_mem));
            });
}

PYBIND11_MODULE(_core, m) {
m.doc() = R"pbdoc(
        syflow python bindings
        -----------------------

        .. currentmodule:: syflow

        .. autosummary::
           :toctree: _generate
    )pbdoc";

py::class_<BgRunnerLoop, std::shared_ptr<BgRunnerLoop>>(m, "BgRunnerLoop")
        .def("run", &BgRunnerLoop::run)
        .def("stop", &BgRunnerLoop::stop);
//        .def_readonly("keep_running", &BgRunnerLoop::keep_running)
//        .def("run_thread", &BgRunnerLoop::run_thread)
//        .def("prepare_to_stop", &BgRunnerLoop::prepare_to_stop)
//        .def("cleanup", &BgRunnerLoop::cleanup);
py::class_<Pipeline>(m, "Pipeline")
        .def(py::init())
        .def("Start", &Pipeline::Start)
        .def("Stop", &Pipeline::Stop)
        .def_readonly("running", &Pipeline::running)
        .def_readwrite("source", &Pipeline::source)
        .def_readwrite("sink", &Pipeline::sink)
        .def_readwrite("processors", &Pipeline::processors);
py::class_<ImageSource, BgRunnerLoop, std::shared_ptr<ImageSource>>(m, "ImageSource")
        .def_readwrite("output_queue", &ImageSource::output_queue)
        .def_readonly("images_pushed", &ImageSource::images_pushed)
        .def("prepare_to_stop", &ImageSource::prepare_to_stop)
        .def("push_blocking", &ImageSource::push_blocking)
        .def("push_nonblocking", &ImageSource::push_nonblocking);
py::class_<ImageSink, BgRunnerLoop, std::shared_ptr<ImageSink>>(m, "ImageSink")
        .def_readonly("input_queue", &ImageSink::input_queue)
        .def_readonly("images_popped", &ImageSink::images_popped);
py::class_<ImageProcessor, ImageSource, ImageSink, std::shared_ptr<ImageProcessor>>(m, "ImageProcessor")
        .def("prepare_to_stop", &ImageProcessor::prepare_to_stop);
py::class_<CameraSource, ImageSource, std::shared_ptr<CameraSource>>(m, "CameraSource")
        .def_property_readonly("name", &CameraSource::getName)
        .def_property_readonly("description", &CameraSource::getDescription);
py::class_<CameraAPI, std::shared_ptr<CameraAPI>>(m, "CameraAPI")
        .def_property_readonly("name", &CameraAPI::getAPIName)
        .def("getCameras", &CameraAPI::getCameras);
py::class_<OpticalFlowUploader, ImageProcessor, std::shared_ptr<OpticalFlowUploader>>(m, "OpticalFlowUploader")
        .def(py::init<int>(), py::arg("block_size"));
py::class_<OpticalFlowExecutor, ImageProcessor, std::shared_ptr<OpticalFlowExecutor>>(m, "OpticalFlowExecutor")
        .def(py::init());
py::class_<DummyImageSink, ImageSink, std::shared_ptr<DummyImageSink>>(m, "DummyImageSink")
        .def(py::init());
py::class_<FileImageSource, ImageSource, std::shared_ptr<FileImageSource>>(m, "FileImageSource")
        .def_readwrite("preload", &FileImageSource::preload)
        .def(py::init<std::vector<std::string>&&>());
py::class_<ThreadSafeQueue<std::shared_ptr<OpticalFlowImage>>>(m, "ThreadSafeQueue")
        .def("size", &ThreadSafeQueue<std::shared_ptr<OpticalFlowImage>>::size)
        .def("clear", &ThreadSafeQueue<std::shared_ptr<OpticalFlowImage>>::clear)
        .def("try_pop", [](ThreadSafeQueue<std::shared_ptr<OpticalFlowImage>> &queue) -> std::optional<std::shared_ptr<OpticalFlowImage>> {
            std::shared_ptr<OpticalFlowImage> image;
            if (queue.try_pop(image)) {
                return image;
            } else {
                return std::nullopt;
            }
        })
        .def("pop", [](ThreadSafeQueue<std::shared_ptr<OpticalFlowImage>> &queue) {
            std::shared_ptr<OpticalFlowImage> image;
            queue.pop(image);
            return image;
        })
        .def("try_push", [](ThreadSafeQueue<std::shared_ptr<OpticalFlowImage>> &queue, std::shared_ptr<OpticalFlowImage>& image) {
            return queue.try_push(std::move(image));
        })
        .def("push", [](ThreadSafeQueue<std::shared_ptr<OpticalFlowImage>> &queue, std::shared_ptr<OpticalFlowImage>& image) {
            queue.push(std::move(image));
        });
declare_cpu_image_owned<uint8_t>(m, "CPUImageOwned_uint8");
declare_cpu_image_owned<S105Vector>(m, "CPUImageOwned_S105Vector");
py::class_<OpticalFlowImage, std::shared_ptr<OpticalFlowImage>>(m, "OpticalFlowImage")
        .def_readwrite("cpu_image", &OpticalFlowImage::cpu_image)
        .def_readwrite("float_vecs", &OpticalFlowImage::float_vecs)
        // GetGpuImageRef and GetGpuFlowVectorsRef does not work from Python, it results in error:
        // numba.cuda.cudadrv.driver.CudaAPIError: [1] Call to cuPointerGetAttribute results in CUDA_ERROR_INVALID_VALUE
        // I think this is because the nvcuvid allocates the Optical Flow buffers with its own special allocator
        // that causes cuPointerGetAttribute to be invalid
        .def("GetGpuImageRef", &OpticalFlowImage::GetGpuImageRef)
        .def("GetGpuFlowVectorsRef", &OpticalFlowImage::GetGpuFlowVectorsRef);
declare_cuda_image_owned<Point<float>>(m, "CudaImageOwned_PointFloat", 2, "<f4");
declare_cuda_image_ref<S105Vector>(m, "CudaImageRef_S105Vector", 2, "<i2");
declare_cuda_image_ref<uint8_t>(m, "CudaImageRef_uint8", 1, "u1");

#ifdef VERSION_INFO
m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
m.attr("__version__") = "dev";
#endif
}
import syflow
from numba import cuda
import math

cuda.select_device(0)

@cuda.jit
def cuda_func(array):
    y, x = cuda.grid(2)
    if y < array.shape[0] and x < array.shape[1]:
        array[y, x, 0] += 10

p = syflow.Pipeline()
p.source = syflow.FileImageSource(['/home/user/Downloads/piv/CTS_tension_00001.png', '/home/user/Downloads/piv/CTS_tension_00002.png'])
p.source.preload = True
p.processors = [syflow.OpticalFlowUploader(4), syflow.OpticalFlowExecutor()]
p.sink = syflow.DummyImageSink()

p.Start()

while True:
    img = p.sink.input_queue.try_pop()
    if img:
        gpu_flow_vecs_managed = img.GetGpuImageRef()
        if gpu_flow_vecs_managed:
            gpu_flow_vecs = cuda.from_cuda_array_interface(gpu_flow_vecs_managed.__cuda_array_interface__,
                                                           owner=gpu_flow_vecs_managed)
            height = gpu_flow_vecs.shape[0]
            width = gpu_flow_vecs.shape[1]

            threadsperblock = (16, 16)
            blockspergrid_y = math.ceil(height / threadsperblock[0])
            blockspergrid_x = math.ceil(width / threadsperblock[1])
            print(gpu_flow_vecs.__cuda_array_interface__)
            print(f'before: {gpu_flow_vecs.copy_to_host()[0,0]}')
            cuda_func[(blockspergrid_y, blockspergrid_x), threadsperblock](gpu_flow_vecs)
            print(f'after: {gpu_flow_vecs.copy_to_host()[0,0]}')
            print('----------')

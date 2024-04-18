"""GPU utils"""

import unittest
import os
from pynvml import nvmlDeviceGetHandleByIndex, nvmlDeviceGetMemoryInfo, nvmlInit
import GPUtil




def gpu_ok(min_memory=1024):
    """Return True, if gpu min_memory is available to use.
    First check if env is set to use cpu:runc or gpu:nvidia,
    then check if gpu memory is available.
    """
    runtime = os.environ.get("RUNTIME")
    print("runtime:", runtime)
    if runtime != "runc":  # nvidia or None
        gpu_avilable_gb = get_gpu_available(0)
        min_memory_gb = min_memory // 1024  # MB to GB

        if gpu_avilable_gb > min_memory_gb:
            print(f"***GPU mode, {gpu_avilable_gb} GB available***")
            return True
    print("***CPU mode***")
    return False

def select_device_tf(min_memory=1024, memory_limit=None, use_gpu=True):
    """selects the device to run on for a given framework - tensorflow
    Returns the selected device.
    """
    import tensorflow as tf
    # Check if device is already selected
    device = os.environ.get("TF_DEVICE_SET")
    if device:
        if device == "gpu":
            print("Tensorflow device already selected as GPU")
            return tf.config.experimental.list_logical_devices("GPU")
        if device == "cpu":
            print("Tensorflow device already selected as CPU")
            return "cpu"
    # Select device
    if use_gpu:
        use_gpu = gpu_ok(min_memory)
        if use_gpu:
            gpus = tf.config.experimental.list_physical_devices("GPU")
            if gpus:
                if memory_limit is None:
                    tf.config.experimental.set_memory_growth(gpus[0], True)
                else:
                    tf.config.experimental.set_virtual_device_configuration(
                        gpus[0],
                        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=memory_limit)],
                    )
                # if len(gpus) > 1:
                #     tf.config.experimental.set_visible_devices(gpus[0], "GPU")
                os.environ["TF_DEVICE_SET"] = "gpu"
                logical_gpus = tf.config.experimental.list_logical_devices("GPU")
                print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
                print("Tensorflow can run in GPU mode")
                return logical_gpus
    # Default use CPU
    tf.config.experimental.set_visible_devices([], "GPU")
    os.environ["TF_DEVICE_SET"] = "cpu"
    print("Tensorflow can run in CPU mode")
    return "cpu"

def select_device_pytorch(use_gpu=True, min_memory=1024, memory_limit=None):
    """selects the device to run on for a given framework - pytorch.
    Returns the selected device.
    """
    import torch
    if use_gpu:
        use_gpu = gpu_ok(min_memory)
        if use_gpu:
            arg = "cuda:0"
            if arg != "cpu" and torch.cuda.is_available():
                arg = "cuda:0"
                if memory_limit:
                    print("WARNING: memory_limit is not supported for PyTorch")
                print("Pytorch can run in GPU mode")
                return torch.device(arg)
    print("Pytorch can run in CPU mode")
    return torch.device("cpu")


def get_gpu_temp():
    """Returns the gpu temperature in celsius"""
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            print("GPU temperature:", gpu.temperature)
            return gpu.temperature
    except:

        print("No GPU available for temp check")
    return 0


def get_gpu_available(index=0):
    """Returns the memory info for the provided GPU (default gpu-index is 0)"""
    try:
        nvmlInit()
        h = nvmlDeviceGetHandleByIndex(index)
        info = nvmlDeviceGetMemoryInfo(h)
        print("GPU memory:")
        print(f"    total    : {info.total//1024**3}")
        print(f"    free     : {info.free//1024**3}")
        print(f"    used     : {info.used//1024**3}")
        return info.free // 1024**3
    except:
        print("CPU only available")
        return 0


class TestGpuUtils(unittest.TestCase):
    """Test methods"""

    def test_get_gpu_temp(self):
        """assert_gpu_temp"""
        temp = get_gpu_temp()
        self.assertLess(temp, 80)

    def test_get_gpu_available(self):
        """get_gpu_available"""
        get_gpu_available(index=0)

    def test_gpu_ok(self):
        """test gpu_ok"""
        print("GPU : ", gpu_ok( min_memory = 1024))

    # def test_select_device_tf_gpu(self):
    #     """test select_device_tf gpu set"""
    #     device = select_device_tf(min_memory=1024, memory_limit=None, use_gpu=True)
    #     print("TF device:", device)
    #     tensor_a = tf.constant([1, 2, 3])
    #     print("tensor_a:", tensor_a)
    #     print("tensor_a.device:", tensor_a.device)

    # def test_select_device_tf_cpu(self):
    #     """test select_device_tf cpu set"""
    #     device = select_device_tf(min_memory=1024, memory_limit=None, use_gpu=False)
    #     print("TF device:", device)
    #     tensor_a = tf.constant([1, 2, 3])
    #     print("tensor_a:", tensor_a)
    #     print("tensor_a.device:", tensor_a.device)

    # def test_select_device_pytorch_gpu(self):
    #     """test select_device_pytorch gpu set"""
    #     device = select_device_pytorch(min_memory=1024, memory_limit=None, use_gpu=True)
    #     print("Pytorch device:", device)
    #     tensor_a = torch.Tensor([1, 2, 3]).to(device)
    #     print("tensor_a:", tensor_a)


if __name__ == "__main__":
    test_obj = TestGpuUtils()
    test_obj.test_get_gpu_temp()
    test_obj.test_get_gpu_available()
    test_obj.test_gpu_ok()
    # test_obj.test_select_device_tf_cpu()
    # test_obj.test_select_device_tf_gpu()
    # test_obj.test_select_device_pytorch_gpu()

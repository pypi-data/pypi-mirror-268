# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : docker_utils.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To handle basic docker functionalitys like bringdown_container, bringup_container etc,."""
import unittest
from time import sleep
import docker

# docker docu: https://docker-py.readthedocs.io/en/stable/containers.html


class DockerManager:
    """wraps the `docker` library and provides a convenient interface to manage docker containers"""

    def __init__(self, image="bfirsh/reticulate-splines", **kwargs):
        self.client = docker.from_env()
        self.container = None
        self.docker_up(image, **kwargs)

    def docker_up(self, image="bfirsh/reticulate-splines", **kwargs):
        """Method to bring up docker container."""
        # Check if container is already running
        if self.container is None:
            # Create docker container
            self.container = self.client.containers.run(image, detach=True, **kwargs)
            self.container_name = self.container.name
            # Wait for container to start
            while True:
                try:
                    self.client.api.inspect_container(self.container_name)
                    break
                except:
                    sleep(1)
            print(f"Container: {self.container_name}- up and running")
        else:
            self.container_name = self.container.name
            print("Container: {self.container_name}- already running")
        print(self.container.logs())

    def docker_down(self):
        """Method to bring down docker container."""
        print(f"Bringing down container: {self.container_name}")
        if self.container is not None:
            self.container.stop()
            self.container.remove()
            self.container = None
        else:
            print("Container already down")
        print("Container list:", self.client.containers.list())
        if len(self.client.containers.list()):
            print("Use: docker rm -f docker_id")

    def __del__(self):
        self.docker_down()


def bringdown_container(container_name: str):
    """Method to bringdown a container with given container name."""
    client = docker.from_env()
    for container in client.containers.list():
        if container.name == container_name:
            print(f"Bringing down {container_name}")
            container.stop()


def docker_gpu_check():
    """Method to check whether GPU is available using docker.
    Returns True if gpu is available else False.
    """
    client = docker.from_env()
    response = client.containers.run(
        "nvidia/cuda:10.1-base-ubuntu18.04",
        "nvidia-smi -L",
        device_requests=[docker.types.DeviceRequest(device_ids=["0"], capabilities=[["gpu"]])],
    )
    if response[:3] == b"GPU":
        return True
    return False


class TestDockerUtils(unittest.TestCase):
    """Test Methods"""

    def test_docker_manager(self):
        """Testing Docker Utils functions - Bringing up and bringing
        down of the docker container and deleting the container"""
        docker_sample = DockerManager(image="bfirsh/reticulate-splines", name=None, ports={"9000/tcp": 9000})
        assert docker_sample is not None, "No Docker object found"

    def test_docker_gpu_check(self):
        """Test docker gpu check - To check whether GPU is available or not using docker"""
        docker_gpu_check()


if __name__ == "__main__":
    test_obj = TestDockerUtils()
    test_obj.test_docker_manager()
    test_obj.test_docker_gpu_check()

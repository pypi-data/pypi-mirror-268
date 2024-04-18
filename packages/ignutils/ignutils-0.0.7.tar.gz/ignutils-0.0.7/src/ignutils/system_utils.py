# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : system_utils.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------

"""Utilits for cmd execution."""
import sys
import shlex
import subprocess
import docker
from easyprocess import EasyProcess

PIPE = subprocess.PIPE


def easyprocess_cmd(cmd):
    """Easyprocess based command"""
    p = EasyProcess(cmd).call()
    stdout = p.stdout
    stderr = p.stderr
    return_code = p.return_code
    return stdout, return_code, stderr


def subprocess_cmd(cmd):
    """run cmd in a subprocess and return the outputs(TODO: description on outputs)"""
    print(f"Command: {cmd}")
    cmd_list = cmd.split()
    with subprocess.Popen(cmd_list, stdout=PIPE, stderr=PIPE, encoding="utf-8") as process:
        stdoutput, stderroutput = process.communicate()
    if process.returncode != 0:
        print(f"Command failed- stdoutput:{stdoutput}, stderroutput:{stderroutput}")
    else:
        print("Command run successfully.")

    return process.returncode, stdoutput, stderroutput


def subprocess_check_call(cmd):
    """run cmd in a subprocess and return the outputs(TODO: description on outputs)"""
    cmd_list = cmd.split()
    return subprocess.check_call(cmd_list)


def subprocess_popen(cmd, start_new_session=True):
    """run cmd in a subprocess and return the process object"""
    cmds = shlex.split(cmd)
    return subprocess.Popen(cmds, start_new_session=start_new_session)


def check_service_available(container_name, exit_flag=True):
    """Check container is Up"""
    try:
        client = docker.from_env()
    except:
        print("\033[91m" + f"{container_name} docker is not available or not granted access. Please check by running docker run hello-world. Try disabling -triton to avoid this." + "\033[91m")
        if exit_flag:
            sys.exit()
        else:
            return None

    for container in client.containers.list():
        if container.name == container_name:
            print(f"Triton Service{container_name} is UP..!")
            return container
    print(f"{container_name} docker is not available")
    return None

def main():
    """Main function"""
    cmd_ = "docker version --format '{{json .}}'"
    # ret, stdout,stderr = subprocess_cmd(cmd)
    # print('ret:',ret)
    # print('stdout:',stdout)
    # print('stderr:',stderr)
    # os.system("docker version --format '{{json .}}'")
    stdout_, return_code_, stderr_ = easyprocess_cmd(cmd_)
    print("stdout_:", stdout_)
    print("return_code_:", return_code_)
    print("stderr_:", stderr_)

if __name__ == "__main__":
    main()

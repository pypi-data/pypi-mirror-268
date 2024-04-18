""" ssh related utils"""
import os
import argparse
import unittest
import subprocess


def ping_test(server_ip="192.168.38.9"):
    """ping test"""
    response = os.system("ping -c 1 " + server_ip)
    # and then check the response...
    if response == 0:
        print("Network Active")
        return True
    print("Network Error")
    return False


class SshfsMnt:
    """Class for mounting and unmounting sshfs filesystems"""

    def __init__(self, local_data_directory="~/mnt3", host_username="jadmin", host_pwd=None, host_ip="192.168.38.9", host_data_directory="/home/jadmin/shared", ssh_copy_id=True):
        """initialize the class
        Assuming you have done ssh-copy-id to the remote server
        Args:
            local_data_directory : local folder to mount.
            host_username : remote server user
            host_ip : remote server ip
            host_data_directory : remote server folder to mount.
        """
        self.local_data_directory = local_data_directory
        self.host_ip = host_ip
        self.host_username = host_username
        self.host_pwd = host_pwd
        self.host_data_directory = host_data_directory
        self.ssh_copy_id = ssh_copy_id
        self.unmount_command = f"fusermount -u  {local_data_directory}"
        if not ping_test(self.host_ip):
            raise ValueError("[!] Error, Unable to ping server, Verify if ip is correct")

        if self.ssh_copy_id:
            ls_command = f"ssh {self.host_username}@{self.host_ip} ls"
            copy_id_command = f"ssh-copy-id {host_username}@{host_ip}"
            print("copy_id_command: ", copy_id_command)
            response = self.sub_process(copy_id_command)
            assert response == 0
        mkdir_command = f"mkdir {local_data_directory} -p"
        self.sub_process(mkdir_command)

        mkdir_command = f"ssh {self.host_username}@{self.host_ip} mkdir -p {host_data_directory}"
        response = self.sub_process(mkdir_command)
        # assert response == 0, "Unable to create directory on remote server"

        mount_command = f"sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 {host_username}@{host_ip}:{host_data_directory} {local_data_directory}"

        # mount_command = 'sshfs -o allow_other -o IdentityFile={} {}@{}:{} {}'.format(
        # key_file, host_username, host_ip, host_data_directory, local_data_directory)

        response = self.sub_process(mount_command)

    def sub_process(self, command):
        """sshpass subprocess"""
        if not self.ssh_copy_id:
            command = f"sshpass -p {self.host_pwd} {command}"
        return subprocess.call(command, shell=True)

    def test(self, test_dir):
        """Creating a directory on the remote server and checking locally in mounted foler"""
        test_dir = os.path.join(self.host_data_directory, "test")
        print("Creating test directory in remote server")
        mkdir_command = f"ssh {self.host_username}@{self.host_ip} mkdir -p {test_dir}"
        response = self.sub_process(mkdir_command)
        ls_command = f"ls {self.local_data_directory}"
        response = self.sub_process(ls_command)
        assert os.path.exists(os.path.join(os.path.expanduser(self.local_data_directory), "test")), "test directory not found"
        print("test directory found in local too")

    def __del__(self):
        print("Unmounting...", self.unmount_command)
        try:
            subprocess.call(self.unmount_command, shell=True)
        except:
            print(f"try- sudo umount -l {self.local_data_directory}")
            subprocess.call(f"umount {self.local_data_directory}", shell=True)


def argument_parser():
    """Argument Parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-user", "--host_user", type=str, help="hostname", required=True)
    parser.add_argument("-pw", "--password", type=str, help="host user password", required=True)
    parser.add_argument(
        "-ip",
        "--host_ip",
        type=str,
        default="192.168.38.7",
        help="host ip",
    )
    return parser.parse_args()


class TestSshUtils(unittest.TestCase):
    """Test ssh utils functions"""

    @classmethod
    def setUpClass(cls):
        args = argument_parser()
        cls.host_username = args.host_user
        cls.pwd = args.password
        cls.host_ip = args.host_ip
        print(f"Username: {cls.host_username}, Password: {cls.pwd}")

    def test_ssh_mnt(self):
        """Testing ssh mount function"""
        sshfs = SshfsMnt(local_data_directory="~/mnt3", host_username=self.host_username, host_pwd=self.pwd, host_ip=self.host_ip, host_data_directory=f"/home/{self.host_username}/shared", ssh_copy_id=False)
        # sshfs.test() ## Test dir ##
        del sshfs
        print("done")

    def test_ping_test(self):
        """Testing ping test"""
        ping_test(server_ip="192.168.38.9")

    def test_subprocess(self):
        """testing from a subprocess command"""
        command = "ssh-keyscan 10.201.1.150"
        response = subprocess.call(command, shell=True)
        print(response)


if __name__ == "__main__":
    test_obj = TestSshUtils()
    test_obj.setUpClass()
    test_obj.test_ssh_mnt()
    test_obj.test_ping_test()
    test_obj.test_subprocess()

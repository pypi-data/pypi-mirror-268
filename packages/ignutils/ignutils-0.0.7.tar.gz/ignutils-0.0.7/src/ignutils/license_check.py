# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : license_check.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To validate the license."""

import json
import os
import os.path as osp
import platform
import subprocess
import sys
import time
import unittest
from datetime import date, datetime, timezone

import ntplib
from cryptography.fernet import Fernet

# import easygui
from dateutil.relativedelta import relativedelta

CWD = os.getcwd()


class LicenceTimeCheck:
    """A class for checking if a licence has expired."""

    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        """Licence end date and time as input"""
        end_dt = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)
        self.end_ts = end_dt.timestamp()
        self.curr_ts = self.get_time()

    def get_time(self):
        """Get the current time by querying an NTP server."""
        while True:
            try:
                c = ntplib.NTPClient()
                response = c.request("pool.ntp.org")
                return response.tx_time
            except:
                print("Error getting time")
                time.sleep(1)

    def valid_licence(self):
        """Checks if the current time is before the end time of the license."""
        return bool(self.curr_ts < self.end_ts)

class LicenseGen:
    """A class that generates a license key for a software application"""

    def __init__(self, jetsonflag=True):
        self.bad_chars = ["(", ")", " ", "'", "\\n"]
        # self.key = Fernet.generate_key()
        self.key = "NOwmbn86RpEIl2o2bYjZmeFa-2ZyPAIzCELXjPlaMN0=".encode()
        self.jetsonflag = jetsonflag
        self.timecheck = False

    def unique_key_generator(self):
        """Generates a unique key for the current system.
        :return: A unique string key for the current system."""
        cpu_id = self.get_system_info()
        unique_id = self.get_unique_id(cpu_id)
        return unique_id

    def secured_encryption(self):
        """Generates a unique key based on system information, encrypts the key using Fernet encryption,
        writes the encrypted key to a temporary file, and returns the encrypted key as a string."""
        unique_id = self.unique_key_generator()
        encrypted = self.get_encrypted(str(unique_id))
        dstfile = osp.join(CWD, "tempkeyfile")
        self.write_to_txt(dstfile, encrypted)
        return encrypted

    def process_id(self, rawdata):
        """Extracts and cleans a specific ID from raw data."""
        info = rawdata.split("   ")[3]
        for i in self.bad_chars:
            info = info.replace(i, "")
        info = info.split(":")[1]
        return info

    def get_system_info(self):
        """Returns the unique identifier for the system."""
        if self.jetsonflag:
            info = self.get_hardware_info()
        elif platform.system() == "Linux":
            command = "sudo dmidecode -t system | grep 'Serial Number'"
            # info = str(subprocess.getstatusoutput(command))
            info = str(subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0]) # pylint: disable=consider-using-with

            info = info.split(":")[1]
            for i in self.bad_chars:
                info = info.replace(i, "")
        elif "Windows" in platform.system():
            # command = "wmic bios get serialnumber"
            command = "wmic csproduct get UUID /format:value"
            info = str(subprocess.getstatusoutput(command))
            # info = info.split('SerialNumber')[-1]
            # print('info: ', info)
            for i in self.bad_chars:
                info = info.replace(i, "")
        cpu_id = info

        return str(cpu_id)

    def read_jsonfile(self, filename):
        """Reads a jsonfile and returns its contents."""
        with open(filename, encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        os.remove(filename)
        return data

    def get_hardware_info(self):
        """Retrieves the hardware information of the device using the 'lshw' command."""
        command = "sudo lshw"
        info = str(subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0]) # pylint: disable=consider-using-with
        ser_num = self.process_id(info)
        return ser_num

    def get_unique_id(self, cpu_id):
        """Returns a unique identifier for the current system"""
        d1 = date.today().strftime("%d_%m_%Y")
        unique_id = " ".join([cpu_id, d1])
        return unique_id

    def get_encrypted(self, message):
        """ "Encrypts a message using the Fernet symmetric encryption algorithm"""
        message = message.encode()
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(message)
        # print('Encrypted key: ', encrypted)
        # print('\n')
        return encrypted

    def get_decrypted(self, encryptedfile):
        """Decrypts an encrypted message using the Fernet symmetric encryption algorithm"""
        encrypted = self.read_from_txt(encryptedfile)
        fernet = Fernet(self.key)
        encrypted = bytes(encrypted)
        decrypted = fernet.decrypt(encrypted)
        decrypted = decrypted.decode("utf-8")
        # print('Decrypted key: ', decrypted)
        return decrypted

    def compare_date(self, system_date, expiry_date):
        """Compare two dates to check if expiry date is later than system date and warn if expiry date is within a week"""
        if self.timecheck:
            d1, m1, y1 = [int(x) for x in system_date.split("_")]
            b1 = date(y1, m1, d1)
            d2, m2, y2 = [int(x) for x in expiry_date.split("_")]
            b2 = date(y2, m2, d2)
            diff_days = (b2 - b1).days
            if 0 < diff_days < 7:
                print(True)
                # easygui.msgbox("License is about to expire in {} days!!".format(diff_days), title="Warning Box")
            if b2 > b1:
                return True
            return False
        return True

    def check_license(self, key):
        """Check whether the license key is valid and has not expired"""
        exp_date = key.split("_")[1]
        exp_date = datetime.fromtimestamp(int(exp_date) / 1000).date()
        today = date.today()
        if today <= exp_date:
            return True

        cpu_id, expirydate = key.split(" ")
        system_cpu_id = self.get_system_info()
        system_date = date.today().strftime("%d_%m_%Y")
        if cpu_id == system_cpu_id:
            # print('cpu id and mac address matched..!')
            if self.compare_date(system_date, expirydate) is True:
                print("License check success..!")
                return True
            print("Your License has expired..!")
                # easygui.msgbox("Your License has expired..!", title="Warning Box")
        else:
            print("License check failed..!")
            # easygui.msgbox("License check failed..!", title="Warning Box")
        return False


    def get_new_encrypted_key(self, key):
        """Generates a new encrypted key based on the given `key`, with an expiry date 12 months from today"""
        cpu_id, date = key.split(" ")
        expiry_date = datetime.today() + relativedelta(months=12)
        expiry_date = expiry_date.strftime("%d_%m_%Y")
        new_key = " ".join([cpu_id, expiry_date])
        # print('New Key: ', new_key)
        return new_key

    def write_to_txt(self, key_file, key):
        """Writes the given `key` to a text file with the specified filename `key_file`"""
        print("key_file: ", key_file)
        with open(key_file, "wb") as f:
            f.write(key)

    def read_from_txt(self, keyfile):
        """Reads the contents of the specified text file and returns them as a bytes object"""
        with open(keyfile, "rb") as f:
            key = f.read()
        return key

    def generate_new_license(self, tempkeyfile):
        """Generates a new license file based on the contents of the specified temporary key file"""
        decrypted_key = self.get_decrypted(tempkeyfile)
        # temp license for 1 month
        new_key = self.get_new_encrypted_key(decrypted_key)
        # encrypted = self.get_encrypted(new_key)
        encrypted = self.get_encrypted("AQ23XC_1651753055000_TF456")
        self.write_to_txt(osp.join(CWD, "licensefile"), encrypted)
        # decrypted_key = license_obj.get_decrypted('licensefile')

class TestLicenseCheck(unittest.TestCase):
    """Test Method for License Check"""
    def test_check_license(self):
        """testing the license check function"""
        license_obj = LicenseGen()
        if os.path.isfile(osp.join(CWD, "licensefile")):
            decrypted_key = license_obj.get_decrypted(osp.join(CWD, "licensefile"))
            license_flag = license_obj.check_license(decrypted_key)
            if not license_flag:
                print("License expired..! Plesae contact Ignitarium ")
                sys.exit()
        else:
            print("No License file found..! Creating a temporary keyfile, contact Ignitarium for getting license")
            encrypted_key = license_obj.secured_encryption()
            sys.exit()

    def test_generate_new_license(self):
        """testing generating new license"""
        license_obj = LicenseGen()
        license_obj.generate_new_license(osp.join(CWD, "tempkeyfile"))

    def test_license_validity(self):
        """testing the license validity"""
        tc = LicenceTimeCheck(2022, 5, 6)
        license_flag = tc.valid_licence()
        print("Licence validity:", license_flag)
        if not license_flag:
            print("License expired..! Plesae contact Ignitarium ")
            sys.exit()


if __name__ == "__main__":
    test_obj = TestLicenseCheck()
    test_obj.test_check_license()
    test_obj.test_generate_new_license()
    test_obj.test_license_validity()

# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : clone_utils.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------

"""Utilits for git cloning and other related ."""
import os
import random
import getpass
import unittest
import argparse
import subprocess
from tqdm import tqdm

from git import Repo
from git import RemoteProgress
from ignutils.yaml_utils import read_yaml, write_yaml
from ignutils.draw_utils import print_colored

PIPE = subprocess.PIPE


## export DB_ACCESS_TOKEN=cPuMRssw5BKeMApXQXei
class CloneRepo:
    """Class for handling cloning of the repo and git commands on cloned repo
    clone_obj = CloneRepo(url=..,branch=..,repo_path=...)
    clone_obj.git_clone()
    clone_obj.get_diff()
    clone_obj.git_add(“.”)
    clone_obj.git_commit(message=’.’) etc..
    """

    def __init__(self, url, branch, repo_path, gitlab_user_name=None, access_token_name=None, access_token_value=None, tmp_path="tmp.yaml", stash_flag=False, pull_flag=True, checkout_flag=False, main_branch="master"):  # "DB_ACCESS_TOKEN",
        """Takes following inputs as self variables for cloning repo"""
        self.branch = branch
        self.tmp_path = tmp_path
        self.new_credentials = False
        self.repo_path = repo_path
        self.main_branch = main_branch
        self.checkout_flag = checkout_flag  # To checkout to the given branch name, if current head is in another branch
        self.access_token_name = access_token_name
        self.access_token_value = access_token_value

        self.ci_job_token = os.environ.get("CI_JOB_TOKEN")
        self.gitlab_user_name = os.environ.get("GITLAB_USER_NAME")
        if self.gitlab_user_name is None:
            self.gitlab_user_name = gitlab_user_name
        if access_token_name is not None:
            self.access_token_value = os.environ.get(access_token_name)
            if self.access_token_value is not None:
                print(f"Got access token {self.access_token_name} from env!")
            elif access_token_value is not None:
                self.access_token_value = access_token_value
                print(f"Got access token {self.access_token_name} and value as input")
            else:
                print(f"Cant find access token {self.access_token_name} in env...")
        elif access_token_value is not None:
            self.access_token_value = access_token_value
            print("Got access token value as input")
        if os.path.exists(self.tmp_path):
            self.user, self.pw = self._read_credentials()  # pylint: disable=C0103
        elif self.ci_job_token is None and self.access_token_value is None:
            # get user name and pw from user
            self.user, self.pw = self._get_credentials()
        else:
            self.user, self.pw = None, None

        print("ci_job_token:", self.ci_job_token)
        print("gitlab_user_name:", self.gitlab_user_name)
        print("access_token_name", access_token_name)
        self.org_url = url

        # Change input url to one with credentials
        if self.ci_job_token:
            print("using gitlab-ci-token")
            url = "https://" + "gitlab-ci-token" + ":" + self.ci_job_token + "@" + url[8:]
        elif self.gitlab_user_name and self.access_token_value:
            print(f"using {self.gitlab_user_name} and access token: {self.access_token_name}")
            url = "https://" + self.gitlab_user_name + ":" + self.access_token_value + "@" + url[8:]
        elif self.user and self.pw:
            print(f"using username: {self.user} and user password")
            url = "https://" + self.user + ":" + self.pw + "@" + url[8:]
        else:
            raise ValueError("Unable to find user credentials")
        self.url = url

        # print("clone url:", self.url)
        print("repo path:", repo_path)

        self.git_clone()

        # Check differences between current files and last commit
        diff = self.get_diff()
        if diff:
            print("diffs:", len(diff))

        if stash_flag:
            self.git_stash()

        if self.repo.is_dirty(untracked_files=True):
            print("Changes detected, ")

        if pull_flag:
            self.git_pull()
        if self.new_credentials:  # write credentials for reuse
            write_yaml(self.tmp_path, config={"user": self.user, "pw": self.enc})

    def git_clone(self):
        """Clone repo"""
        if not os.path.exists(self.repo_path):
            print("Cloning the repo:", self.org_url, "with branch:", self.branch, "to path:", self.repo_path)
            self.repo = Repo.clone_from(self.url, self.repo_path, branch=self.branch, depth=1, progress=CloneProgress())
        else:
            self.repo = Repo(self.repo_path)
            self.git_checkout()
            print(f"Skipping clone of {self.repo_path}, its already existing.")

    def get_diff(self):
        """get diffs in repo"""
        diff = self.repo.git.diff(self.repo.head.commit.tree)
        diff = None if diff == "" else diff
        return diff

    def get_branchnames(self):
        """Returns all available branch names in the repository"""
        branches = self.repo.references
        branchnames = [branch.name for branch in branches]
        return branchnames

    def git_checkout(self):
        """Checkout to a specific branchname"""
        current = self.repo.create_head(self.branch)
        current.checkout()

    def git_add(self, input_=None):
        """git add based on input_, can be: '-u', '.', file list"""
        print(f"git add {input_} to {self.repo_path}")
        self.repo.git.add(input_)

    def git_pull(self):
        """git pull"""
        print(f"git pull in {self.repo_path}")
        if self.repo.is_dirty(untracked_files=False):
            print_colored("There are changes in repo, skipping pull", color="yellow")
        else:
            # origin_ = self.repo.remote(name="origin")
            # for fetch_info in origin_.pull(progress=CloneProgress()):
            #     print(f"Updated {fetch_info.ref} to {fetch_info.commit}")
            try:
                print(self.repo.remotes.origin.pull())
                # print("Pulled changes to repo:", self.repo_path)
                print_colored(f"***** Pulled changes to repo:{self.repo_path}", color="green")
            except Exception as e:
                raise ValueError("Pull failed : ") from e

    def git_stash(self):
        """git stash"""
        print(f"git stash in {self.repo_path}")
        self.repo.git.stash()
        print("Stashed changes in repo:", self.repo_path)

    def git_push(self):
        """To push to remote"""
        print(f"git push in {self.repo_path}")
        origin_ = self.repo.remote(name="origin")
        origin_.push()
        print("Pushed changes to repo:", self.url)

    def git_commit(self, message):
        """Function to commit the changes to the repo"""
        print(f"git commit in {self.repo_path}, message:{message}")
        self.repo.index.commit(message)

    def _get_credentials(self):
        """To get git credentials."""
        user = input("Username for 'https://gitlab.ignitarium.in': ")
        self.user = self._sanity_str(user)
        pw = getpass.getpass(prompt="Password for 'https://gitlab.ignitarium.in': ")
        pw = self._sanity_str(pw)
        self.enc = pw.encode(encoding="ibm424")
        self.new_credentials = True
        return self.user, pw

    def _read_credentials(self):
        """Read credentials from tmp folder"""
        if os.path.exists(self.tmp_path):
            config = read_yaml(self.tmp_path)
            user = config["user"]
            enc = config["pw"]
            pw = enc.decode(encoding="ibm424")
        else:
            raise ValueError(f"{self.tmp_path} missing.")
        return user, pw

    def _sanity_str(self, word):
        """To check sanity for string."""
        special = ["!", "#", "$", "&", "'", "(", ")", "*", "+", ",", "/", ":", ";", "=", "?", "@", "[", "]"]  # pylint: disable=C0301
        replacement = ["%21", "%23", "%24", "%26", "%27", "%28", "%29", "%2A", "%2B", "%2C", "%2F", "%3A", "%3B", "%3D", "%3F", "%40", "%5B", "%5D"]  # pylint: disable=C0301
        newword = []

        for char in word:
            if char in special:
                newword.append(replacement[special.index(char)])
            else:
                newword.append(char)
        # char list to word
        new = ""
        new = new.join(newword)
        # for x in newword:
        #     new +=x
        newword = new
        return newword


class CloneProgress(RemoteProgress):
    """clone progress class for git clone"""

    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=""):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()


def get_args():
    """Reads the user arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-url",
        "--repo_url",
        type=str,
        default="https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/",
        help="repo to be cloned",
    )
    parser.add_argument(
        "-b",
        "--branch",
        type=str,
        default="Scopito_dummy",
        help="repo to be cloned",
    )
    parser.add_argument(
        "-p",
        "--repo_path",
        type=str,
        default="workspace/db/",
        help="path to which repo is to be cloned",
    )
    parser.add_argument(
        "-stash",
        "--stash_flag",
        default=False,
        nargs="?",
        const=True,
        help="To stash DB, weights, sample videos etc.,",
    )
    parser.add_argument(
        "-pull",
        "--pull_flag",
        default=False,
        nargs="?",
        const=True,
        help="To pull DB, weights, sample videos etc.,",
    )
    parser.add_argument(
        "-user",
        "--gitlab_user_name",
        type=str,
        default=None,
        help="gitlab_user_name",
    )
    parser.add_argument(
        "-atn",
        "--access_token_name",
        type=str,
        default="DB_CLONE_TOKEN",
        help="access_token_name",
    )
    parser.add_argument(
        "-atv",
        "--access_token_value",
        type=str,
        default=None,
        help="access_token_value",
    )
    args = parser.parse_args([])
    return args


class TestCloneRepo(unittest.TestCase):
    """Test methods"""

    def test_clone_repo(self):
        "Tests to check all the git related functions"
        # args = get_args()
        ### Git clone test - heppens inside init itself ###
        repo_path = "samples/test_results/clone_test_results"
        clone_obj = CloneRepo(url="https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db/", branch="unittest_db", repo_path=repo_path)
        assert os.path.isdir(repo_path)
        # ## Testing diff ##
        print()
        file_path = os.path.join(repo_path, "sample_test.txt")
        with open(file_path, "w", encoding="utf-8") as file_object:
            val = random.random()
            file_object.write("Sample file for testing the Clone utils module - new line " + str(val) + "\n")
        file_object.close()
        diff = clone_obj.get_diff()
        if diff:
            print("Changes Detected")
            print(len(diff))
            assert len(diff) > 0, "Changes not added"
        # ## Tesing add commit and push ##
        print()
        clone_obj.git_add(".")
        clone_obj.git_commit(message="Adding extra line")
        # clone_obj.git_push()
        ## Testing stash ##
        print()
        with open(file_path, "w", encoding="utf-8") as file_object:
            file_object.write("Adding line to stash\n")
        file_object.close()
        diff = clone_obj.get_diff()
        if diff:
            clone_obj.git_stash()
        diff = clone_obj.get_diff()
        assert diff is None
        ## Testing git pull ##
        print()
        clone_obj.git_pull()


if __name__ == "__main__":
    test_obj = TestCloneRepo()
    test_obj.test_clone_repo()

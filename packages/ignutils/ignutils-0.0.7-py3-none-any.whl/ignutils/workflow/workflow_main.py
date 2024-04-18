"""
infer_workflow.py(project, nodelist):
            init: create node_infer object dictionary.
            run: calls infer on each node using full image and json, overlay on full image, writes to results/workflow/projectname/input folder name
"""
import os
import os.path as osp
import unittest
import argparse
import cv2
from loguru import logger
from ignutils.labelme_utils import write_label_json, create_labelme_json, get_label_count
from ignutils.file_utils import change_extn, create_directory_safe, get_all_files
from ignutils.json_utils import read_json
from ignutils.workflow.mlnode import get_project_config
from ignutils.workflow.node_utils import  get_positive_negative_files
from ignutils.workflow.keras_seg_mlnode import KerasSegMlNode


class InferWorkflow:
    """class for inference workflow using given nodes or
    all nodes of project"""

    def __init__(
        self,
        projectname,
        project_config_path=None,
        workspace=None,
        nodes=(),
        ex_nodes=(),
        dump_results=True,
        show_flag=False,
        apply_filter=True,
        triton_mode=False,
        print_flag=False,
        git_flag=True,
        gpu_flag=True,
        pull_flag=False,
        stash_flag=False,
        run_mode="infer",
        full_db_flag=False,
        debug_level=0,
    ):
        """create node_infer objects dictionary by looping through node list.
        project: project anme
        node list: nodes to be used, if empty then use all nodes
        workspace: directory to use for writing data/results
        """
        self.print_flag = print_flag
        self.projectname = projectname
        self.debug_level = debug_level
        self.dump_results = dump_results
        self.show_flag = show_flag
        self.apply_filter = apply_filter
        self.triton_mode = triton_mode
        self.workspace = workspace
        self.run_mode = run_mode
        self.full_db_flag = full_db_flag
        if workspace is None:
            workspace = os.path.join("Projects", projectname, "workspace")
            print("workspace was not given, using default:", workspace)

        if project_config_path is None:
            project_config_path = os.path.join("Projects", projectname, projectname + ".yaml")
            print("project_config_path was not given, using default:", project_config_path)

        if dump_results:
            self.result_dir = osp.join(workspace, "Results")
            # TO-DO Add inside inp folder
            create_directory_safe(self.result_dir)
        self.workspace = workspace
        self.project_config_path = project_config_path
        self.get_pix_nodes(projectname, project_config_path, nodes, ex_nodes)
        self.pix_objs = {}
        for node_name in self.pix_nodes:
            # self.pix_objs = []
            node_type = self.project_config["nodes"][node_name]["node_type"]
            # obj_creator: Optional[Type[SegMlNode]]=None
            if node_type == "semseg":
                # sys.path.append("../../yolov5_gitlab")

                obj_creator = KerasSegMlNode

            pix_obj = obj_creator(
                projectname=projectname,
                node_name=node_name,
                project_config_path=project_config_path,
                workspace=workspace,
                print_flag=print_flag,
                git_flag=git_flag,
                gpu_flag=gpu_flag,
                db_pull_flag=pull_flag,
                db_stash_flag=stash_flag,
                debug_level=self.debug_level,
                all_nodes=self.pix_nodes,
                run_mode=self.run_mode,
                full_db_flag=self.full_db_flag,
            )

            self.pix_objs[node_name] = pix_obj
            if print_flag:
                print(node_name, "node created")
        logger.info("workflow initialized, ready to run!")

    def __str__(self):
        """About class, string shown to users (on str and print)"""
        return "Workflow class instance"

    def __repr__(self):
        """About class, string shown to developers (at REPL)"""
        return f"{self.__str__()}.It inits node objects in init and run method \
        for looping through nodes and \
        predicting on full image and full json)"

    def get_pix_nodes(self, projectname, project_config_path, nodes, ex_nodes):
        """get pix nodes from project config
        sets project_config and pix_nodes,
        """
        assert not (nodes and ex_nodes), "Supports either nodes or exclude nodes at a time"
        if project_config_path is None:
            project_config_path = projectname + ".yaml"
            print("project_config_path is not given, so using default:", project_config_path)

        self.project_config = get_project_config(project_config_path, projectname)
        assert self.project_config["projectname"] == projectname, f"{self.project_config['projectname']} not same as {projectname}"

        if not nodes:
            self.pix_nodes = list(self.project_config["nodes"].keys())
        else:
            self.pix_nodes = nodes
        self.pix_nodes = [px for px in self.pix_nodes if px not in ex_nodes]
        # TO-DO For given user nodes, if any child node's parent is not available in pix_nodes, and json_dir is None, throw exception
        print("nodes used:", self.pix_nodes)

    def run_image(self, img, img_path=None, json=None, write_results=True, dump_crops=False):
        """calls infer on each node using full image and json,
        overlay on full image,
        writes to workspace/results/workflow/projectname/input folder name?
        returns update json and overlay image
        """
        overlay_img = img.copy()
        if json is None:
            json = create_labelme_json()
        for inf_key, value in self.pix_objs.items():
            print(inf_key, value)
            inf_obj = self.pix_objs[inf_key]
            overlay_img, json_dict = inf_obj.infer_img_json(img, json, overlay_img, img_path, dump_crops=dump_crops)
        if write_results and self.run_mode == "infer" and img_path is not None:
            print("TODO: write results")
            img_basename = os.path.basename(img_path)
            json_path = change_extn(img_basename, ".json")
            cv2.imwrite(os.path.join(self.result_dir, img_basename), overlay_img)
            write_label_json(os.path.join(self.result_dir, json_path), json_dict, image_path=img_basename)
        return overlay_img, json

    def run_folder(self, folderpath=None, dump_crops=False):
        """Run inference on a folder"""
        if self.run_mode == "dump_data":
            assert folderpath is None, "inp folder must be None while doing data dump"
        if folderpath is None:
            folderpath = os.path.join(self.workspace, "DB", "git_DB_dummy")
            if self.full_db_flag:
                folderpath = os.path.join(self.workspace, "DB", "git_DB_full")
            else:
                folderpath = os.path.join(self.workspace, "DB", "git_DB_dummy")
        files_list = get_all_files(folderpath, include_type="image")
        if self.run_mode == "dump_data":
            dump_crops = True
            for node_name in self.pix_nodes:
                files_list = get_all_files(folderpath, include_type="image", checksum_flag=True, checksum_overwrite=False, checksum_folder=node_name)
                if files_list:
                    node_obj = self.pix_objs[node_name]
                    files_list = get_positive_negative_files(files_list, node_obj.node_config_obj)

        for img_file in files_list:
            print("\nprocessing:", img_file)
            img = cv2.imread(img_file)
            json_file = change_extn(img_file, extn=".json")
            json_dict = create_labelme_json()
            if os.path.isfile(json_file):
                json_dict = read_json(json_file)
            overlay_img, json = self.run_image(img, json=json_dict, img_path=img_file, dump_crops=dump_crops)

    def train(self, epochs):
        """train the current node"""
        for inf_key, value in self.pix_objs.items():
            print(inf_key, value)
            inf_obj = self.pix_objs[inf_key]
            inf_obj.train(epochs)


    def test(self, folderpath):
        """Evaluate keras  model"""
        for inf_key, value in self.pix_objs.items():
            print(inf_key, value)
            inf_obj = self.pix_objs[inf_key]
            inf_obj.test(folderpath)


class WorkflowUnittestBase(unittest.TestCase):
    """Test case for workflow based train and infer for Scopito Wind Turbine detection"""

    __test__ = False
    train_node = "person"
    inference_nodes = ["person"]
    projectname = "person_detection"
    classnames = ["person"]
    project_config_path = "Projects/person_detection/person_detection.yaml"
    from_scratch = False
    workspace = "Projects/person_detection/workspace"
    image_folder = "DB/git_DB_dummy/person_detection/test"
    count = [10]
    epochs = 10

    def test_train_infer_count(self):
        """Unit test for training train node with existing wts and inefrence with  count assert"""
        wf_obj = InferWorkflow(projectname=self.projectname, project_config_path=self.project_config_path, workspace=self.workspace, nodes=[self.train_node], run_mode="dump_data")
        wf_obj.run_folder()
        wf_obj = InferWorkflow(projectname=self.projectname, project_config_path=self.project_config_path, workspace=self.workspace, nodes=[self.train_node], run_mode="train")
        if self.from_scratch:
            if os.path.isfile(os.path.join(wf_obj.workspace, "Weights", self.train_node, "model.h5")):
                os.remove(os.path.join(wf_obj.workspace, "Weights", self.train_node, "model.h5"))
                print("model deleted doing from scratch")
        wf_obj.train(self.epochs)
        self.infer_count_assert()

    def infer_count_assert(self):
        """infer using infer nodes and count assert for detections of train-node"""
        wf_obj = InferWorkflow(projectname=self.projectname, project_config_path=self.project_config_path, workspace=self.workspace, nodes=self.inference_nodes)
        image_dir = os.path.join(wf_obj.workspace, self.image_folder)
        wf_obj.run_folder(image_dir, dump_crops=False)
        result_jsons = get_all_files(os.path.join(wf_obj.workspace, "Results"), include_extns=[".json"])
        total_train_node_count = 0
        for result_json in result_jsons:
            result_json_ = read_json(result_json)
            train_node_count = get_label_count(result_json_, self.classnames)
            total_train_node_count += train_node_count
        print("count: ", total_train_node_count)
        assert total_train_node_count in self.count, f"count  {total_train_node_count} is not matching with actual count range {self.count}"


class PersonUnittest(WorkflowUnittestBase):
    """Test methods"""
    __test__ = True


def get_args():
    """Main function"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--projectname",
        required=True,
        help="Project name Eg; Scopito, LR_Stitcher",
    )
    parser.add_argument(
        "-pc",
        "--project_config",
        default=None,
        help="Project config yaml filepath, default from CWD",
    )
    parser.add_argument(
        "-ws",
        "--work_dir",
        default=None,
        help="overlap threshold in pixels",
    )
    parser.add_argument(
        "-n",
        "--node_name",
        nargs="+",
        default=[],
        help="Provide nodes list, Eg; A1_scopito_wt, scopito_wt_body, scopito_cowling",
    )
    parser.add_argument(
        "-m",
        "--run_mode",
        default="infer",
        help="run mode   Example: infer, train, test",
    )
    parser.add_argument(
        "-im_dir",
        "--image_dir",
        default=None,
        help="Image folder to run workflow",
    )
    parser.add_argument(
        "-f",
        "--full_db_flag",
        default=False,
        nargs="?",
        const=True,
        help="full db or dummy db",
    )
    parser.add_argument("-ep", "--epochs", default=1, type=int, help="Number of epochs required to train ")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    wf_obj = InferWorkflow(projectname=args.projectname, workspace=args.work_dir, nodes=args.node_name, run_mode=args.run_mode, full_db_flag=args.full_db_flag)
    if args.run_mode == "infer":
        wf_obj.run_folder(args.image_dir)
    if args.run_mode == "dump_data":
        wf_obj.run_folder()
    if args.run_mode == "train":
        wf_obj.train(epochs=args.epochs)
        assert len(args.node_name) == 1, "Single node training allowed at a time"
    if args.run_mode == "test":
        wf_obj.test(args.image_dir)

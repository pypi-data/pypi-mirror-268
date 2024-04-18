""""
- mlnode.py(node name, project config):
  - init:
    - Download node weight
    - load model
    - get crop method
    - pre_filter,post_filter
  - train/infer preprocess funcs
  - infer(full img, json):
    - pre-filter parent
    - get crop
    - batch_predict:
      - predict
      - post-filter
      - remap contours
      - update json
      - calculate confusion matrix
      - or
      - Dump: A dump flag to prevent predict and just write instead in infer.py.
            Resize based on train resize factor with train expansion>=infer expansion.
            Compare parent contour with label and reuse label if iou is less.
            write_img_json: over ride this func in each node_dump as per need.
"""
import os
import os.path as osp
import abc
from pathlib import Path
from copy import deepcopy
from typing import Optional
import cv2
from ignutils.clone_utils import CloneRepo
# from ignutils.gpu_utils import select_device_tf as select_device
from ignutils.transform_utils import transform_crop, transform_paste
from ignutils.contour_utils import get_tiled_contours
from ignutils.json_utils import write_json
from ignutils.file_utils import create_directory_safe, make_file_path, check_folder_exists
from ignutils.yaml_utils import read_yaml
from ignutils.draw_utils import draw_polylines
from ignutils.labelme_utils import cleanup_json, create_shape_dict
from ignutils.workflow.node_config import NodeConfig
from ignutils.workflow.node_utils import get_labels, get_tiling_info, check_active_aug_enabled, get_active_aug, get_bg_aug_labels
from ignutils.workflow.filter_utils import FIlterJson


class MlNode(metaclass=abc.ABCMeta):
    """Abstract class for model creation and weight loading
    Implement and override as per node's need.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        projectname: str,
        node_name: str,
        workspace: Path,
        project_config_path: Optional[Path] = None,
        load_model_flag: bool = True,
        dump_results_flag: bool = False,
        show_flag: bool = False,
        git_flag: bool = True,
        gpu_flag: bool = True,
        db_stash_flag: bool = False,
        db_pull_flag: bool = False,
        wt_stash_flag: bool = False,
        wt_pull_flag: bool = False,
        print_flag: bool = True, # pylint: disable=unused-argument
        run_mode: str = "infer",  # "train", "infer",
        debug_level: int = 0, # pylint: disable=unused-argument
        full_db_flag: bool = False,
        dump_parent_crops_flag: bool = False,  # dump parent img crops and json crops
        all_nodes=None,  # pylint: disable=unused-argument # all nodes used in workflow
        remove_fp: bool = False,
        framework: str = "tensorflow",  # [tensorflow, pytorch]
        label_folderpath: str=None, # pylint: disable=unused-argument
    ) -> None:
        """
        weight cloning
        config loading
        load_model
        crop method loading
        pre_filter loading
        post_filter loading
        """
        self.projectname = projectname
        self.node_name = node_name
        self.weight_branch = node_name  # node name same as weight branch
        self.full_db_flag = full_db_flag
        # self.project_config = self.get_project_config(project_config_path,projectname)
        self.workspace = workspace
        self.load_model_flag = load_model_flag
        self.git_flag = git_flag
        self.run_mode = run_mode
        self.weight_dir = osp.join(self.workspace, "Weights", self.weight_branch)
        self.download_weight(self.node_name, self.weight_dir, wt_stash_flag, wt_pull_flag)
        self.db_dir = osp.join(self.workspace, "DB")  # type: ignore # Project DB directory

        self.project_config = get_project_config(project_config_path, projectname)
        model_config_path = osp.join(self.weight_dir, "config.yaml")
        self.node_config_obj = NodeConfig(self.node_name, model_config_path)
        self.node_config_dict = self.node_config_obj.get_data()
        self.node_labels = get_labels(self.node_config_obj)
        # update db_dir based on fulldb flag
        if self.full_db_flag:
            self.git_db_dir = osp.join(self.db_dir, "git_DB_full")  # Git directory(Git data will be fetched here)
            self.db_branch_list = self.node_config_obj("db_branch_full")
            self.node_dir = osp.join(self.db_dir, self.weight_branch + "_full")
        else:
            self.git_db_dir = osp.join(self.db_dir, "git_DB_dummy")
            self.db_branch_list = self.node_config_obj("db_branch_dummy")
            self.node_dir = osp.join(self.db_dir, self.weight_branch + "_dummy")
        self.download_db(stash=db_stash_flag, pull=db_pull_flag)
        #     assert_db_structure()
        # parent_node download - for parent colabels
        self.parent_node = self.project_config["nodes"][self.node_name]["parent_node"]
        if self.parent_node:
            self.parent_model_dir = osp.join(self.workspace, "Weights", self.parent_node)
            self.download_weight(self.parent_node, self.parent_model_dir, wt_stash_flag, wt_pull_flag)
            parent_config_path = osp.join(self.parent_model_dir, "config.yaml")
            self.parent_config = NodeConfig(self.parent_node, parent_config_path)
            self.parent_labels = get_labels(self.parent_config)
            # self.parent_labels = list(set(self.parent_labels))
            # self.parent_background_labels = self.parent_config("negative_co_labels")
        else:
            self.parent_model_dir = None
            self.parent_config = None
            self.parent_labels = ["fullimage"]
            self.parent_background_labels = None

        self.dump_results_flag = dump_results_flag
        self.show_flag = show_flag
        self.dump_parent_crops_flag = dump_parent_crops_flag
        self.framework = framework
        self.conf_matrix = (0, 0, 0)
        self.remove_fp = remove_fp
        # select_device(memory_limit=3000, use_gpu=gpu_flag)
        if self.load_model_flag:
            self.load_model(gpu_flag)
        print(f"Node: {self.node_name} initialized in run mode: {run_mode}!!")
        self.label_folderpath=None

    @abc.abstractmethod
    def load_model(self, gpu_flag):
        """load model,
        override this
        eg:
        model = tf.keras.models.load_model('/tmp/model')
        """
        model = []
        return model

    @abc.abstractmethod
    def predict(self, img_batch):
        """image batch for prediciton
        eg:
        pred_batch = self.model.predict(img_batch)
        """
        pred_batch = []
        return pred_batch

    @abc.abstractmethod
    def create_train_data(self):
        """create training data from crops json and imgs"""
        # pass

    @abc.abstractmethod
    def train(self, epochs=10):
        """create training data from crops json and imgs"""
        # pass

    @abc.abstractmethod
    def update_crop_json(self, pred_batch, json_crops):
        """update crop json with node predictions"""
        return json_crops

    def download_weight(self, weight_branch, weight_dir, stash, pull):
        """get  weights"""
        if self.git_flag:
            self.weight_url = "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/weights"
            CloneRepo(self.weight_url, weight_branch, weight_dir, stash_flag=stash, pull_flag=pull, access_token_name="WEIGHT_CLONE_TOKEN")
        else:
            print("git_flag is false, skipping download_db")

    def download_db(self, stash, pull):
        """download DB based on branches"""
        if self.git_flag:
            self.db_url = "https://gitlab.ignitarium.in/tyqi-platform/tyqi-model/experiments/db"
            # Loop and clone db branches
            assert isinstance(self.db_branch_list, list), "db branch must be list in config.yaml"
            for db_branch in self.db_branch_list:
                db_sub_dir = os.path.join(self.git_db_dir, db_branch)
                CloneRepo(self.db_url, db_branch, db_sub_dir, pull_flag=pull, stash_flag=stash, access_token_name="DB_CLONE_TOKEN")
        else:
            print("git_flag is false, skipping download_db")

    def add_full_img_parent(self, img, json):  # TO-DO move to labelme utils
        """Add fullimg label in json if parent is None"""
        json_copy = json.copy()
        shapes = json_copy["shapes"]
        image_h, image_w = img.shape[:2]
        new_shape = create_shape_dict()
        new_shape["label"] = "fullimage"
        new_shape["points"] = [[0, 0], [image_w, 0], [image_w, image_h], [0, image_h]]
        shapes.append(new_shape)
        return json_copy

    def infer_img_json(self, img, json, overlay_img, filename=None, dump_crops=False):
        """infer on full image and json
        return updated json and overlay image"""
        json_copy = deepcopy(json)
        if self.parent_node is None:
            json_copy = self.add_full_img_parent(img, json_copy)
        if json:
            orignal_json = json.copy()
            # add parent in json if parent None
        else:
            orignal_json = None

        # json = self.pre_filter(json)  # parent filtering
        img_crops, json_crops, tr_list, index_list = self.get_parent_crops(img, json_copy)  # current and parent node colabels needed in crop json

        if dump_crops:  # for dumping img json crops
            self.dump_crop_img_json(img_crops, json_crops, filename)  # crop img and json
        if self.run_mode == "infer":  # for inference
            pred_batch = self.predict(img_crops)
            crop_jsons = self.update_crop_json(pred_batch, json_crops)
            json = cleanup_json(json, self.node_labels)
            filter_obj = FIlterJson(self.node_config_obj)
            crop_jsons = self.post_filter(crop_jsons, filter_obj)  # child filtering
            json = self.update_full_json(json, crop_jsons)
            if orignal_json:
                json = self.update_cm(json, orignal_json, remove_fp=self.remove_fp)

            overlay_img = self.overlay(overlay_img, json)  # node specific
            if self.dump_results_flag:
                self.dump_results(overlay_img, json, cm_based=True, dump_crops=True)
        return overlay_img, json

    def get_parent_crops(self, img, json_dict):
        """get parent node crops, given image and json"""
        crop_imgs, crop_jsons, tr_list = [], [], []
        shape_list = json_dict.get("shapes", [])
        index_list = []
        model_input_h, model_input_w = self.node_config_obj("model_input_HW")
        bg_aug_labels = get_bg_aug_labels(self.node_config_obj)

        # handle full image training-->no parent case
        if self.parent_node is None:
            curr_label_list = self.node_labels
        else:
            curr_label_list = self.node_labels + self.parent_labels

        if bg_aug_labels: #for bg augmentation adding labels to be retained
            curr_label_list = curr_label_list + bg_aug_labels
        tiling_info_dict = get_tiling_info(self.node_config_obj)
        pad_h, pad_w = self.node_config_obj("inference_expansion")
        pad_l, pad_r, pad_t, pad_b = pad_w, pad_w, pad_h, pad_h
        for indx, shape in enumerate(shape_list):
            # print('index',indx, shape['label'])
            if shape["label"] in self.parent_labels:
                contour = shape["points"]
                tiled_contours, tiled_boxes = get_tiled_contours(contour, crop_type=self.node_config_obj("crop_type"), tiling_info=tiling_info_dict)
                for tile_box in tiled_boxes:
                    if not contour:
                        continue
                    crop_image, _, crop_json, tr_mtx = transform_crop(
                        image=img,
                        label_list=curr_label_list,
                        json_dict=json_dict,
                        crop_cntr=tile_box,
                        crop_type=self.node_config_obj("crop_type"),
                        h1=model_input_h,
                        w1=model_input_w,
                        pad_l=pad_l,
                        pad_r=pad_r,
                        pad_t=pad_t,
                        pad_b=pad_b,
                        interpolation=cv2.INTER_NEAREST,
                    )
                    crop_json["imageHeight"] = crop_image.shape[0]
                    crop_json["imageWidth"] = crop_image.shape[1]
                    crop_imgs.append(crop_image)
                    crop_jsons.append(crop_json)
                    tr_list.append(tr_mtx)
                    index_list.append(indx)
        # print("getparent crop_jsons after:", len(crop_jsons))

        return crop_imgs, crop_jsons, tr_list, index_list

    def pre_filter(self, json):
        """pre_filter based on node config, image dimension from json"""
        # json = apply_filter(prefilter_info, json)
        return json

    def post_filter(self, crop_jsons, filter_obj):
        """filter crop json based on post-filters in node config"""
        filtered_crop_jsons = filter_obj.apply_filter(crop_jsons)
        return filtered_crop_jsons

    def update_full_json(self, json, crop_jsons):
        """ "update full json with crop json"""
        for crop_json in crop_jsons:
            json = transform_paste(json, crop_json, label_list=self.node_labels)
        return json

    def update_cm(self, json, orignal_json, remove_fp): # pylint: disable=unused-argument
        """calculate cm for current node
        update json tp fp fn info in each contour dict
        for using in overlay.
        """
        # calculate cm by comparing orig json and current json
        tp, fp, fn = 1, 1, 1
        conf = (tp, fn, fp)
        self.conf_matrix += conf
        print("TODO: implement update_cm, update json with tp fp info")
        return json

    def dump_crop_img_json(self, img_crops, json_crops, filename):
        """dump parent crop and crop json,
        for training current node itself!
        implement this differently for semseg, classifier etc
        as per need of node training dataset
        """
        dump_folder = None
        dump_list = ["train", "val", "test"]
        path_list = filename.split("/")
        for end_folder in dump_list:
            if end_folder in path_list:
                dump_folder = end_folder
                break

        rel_path = os.path.relpath(filename, self.git_db_dir)
        if dump_folder is None:
            raise ValueError("DB structure is valid, expecting images to b in train val test folder")
        # dump_folder = os.path.basename(os.path.dirname(os.path.dirname(rel_path)))
        dump_img_folder = os.path.join(dump_folder, "Imgs")
        for index, (img_crop, json_crop) in enumerate(zip(img_crops, json_crops)):
            if not check_folder_exists(os.path.join(self.node_dir, dump_img_folder)):
                create_directory_safe(os.path.join(self.node_dir, dump_img_folder))
            file_path = make_file_path(file_path=rel_path, dst_path=os.path.join(self.node_dir, dump_img_folder))
            img_path = f"{file_path }_{index}.png"
            json_path = f"{file_path }_{index}.json"
            json_crop["imagePath"] = os.path.basename(img_path)
            write_json(json_path, json_crop)
            cv2.imwrite(img_path, img_crop)
            if check_active_aug_enabled(self.node_config_obj) and 'train' in rel_path.split('/'):
                aug_crop, aug_json = get_active_aug(img_crop, json_crop, self.node_dir, self.node_config_obj, self.git_db_dir)
                aug_img_path = f"{file_path }_{index}_aug.png"
                aug_json_path = f"{file_path }_{index}_aug.json"
                aug_json["imagePath"] = os.path.basename(aug_img_path)
                write_json(aug_json_path, aug_json)
                cv2.imwrite(aug_img_path, aug_crop)

    def overlay(self, overlay_img, json):
        """Overlays polylines on the input image"""
        shapes = json["shapes"]
        classes = self.node_config_obj("classes")
        for shape in shapes:
            if shape["label"] in classes.keys():
                color = classes[shape["label"]]["color"]
                draw_polylines(overlay_img, shape["points"], color=color, fill=False)
        return overlay_img

    def dump_results(self, img, json, cm_based=True, dump_crops=True):
        """dump result img and json
        if cm_based, then write into tp fp fn folders
        if dump_crops, then write child crops as well
        """

    def __str__(self):
        """About class, string shown to users (on str and print)"""
        return f"MlNode obj: {self.node_name}, with parent: {self.parent_node}"

    def __repr__(self):
        """About class, string shown to developers (at REPL)"""
        return self.__str__()


# support functions that are needed in workflow


def get_project_config(project_config_path, projectname):
    """read project coonfig"""
    print("project_config_path:", project_config_path)
    assert os.path.isfile(
        project_config_path
    ), f"{projectname} config is not found in {project_config_path}, \
    please refer ignutils/ignutils/workflow/README.md and create same"
    project_config = read_yaml(project_config_path)
    return project_config

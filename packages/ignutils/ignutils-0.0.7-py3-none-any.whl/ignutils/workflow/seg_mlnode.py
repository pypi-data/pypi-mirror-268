"""
- node/mlnode.py:(workflow/node_type/mlnode)
Inherit and over ride any function of workflow/node_type/mlnode.
Create node/infer object and call its predict/dump dataset
or
load model, preprocess input and predict in mlnode itself
"""
import os
import time
from pathlib import Path
from typing import Optional, Union
import cv2
from ignutils.workflow.mlnode import MlNode
from ignutils.contour_utils import get_contours_multichannel, cv2lab, rescale_contour
from ignutils.labelme_utils import cleanup_json, create_shape_dict, get_index_image
from ignutils.file_utils import get_all_files, check_folder_exists, create_directory_safe
from ignutils.json_utils import read_json

# pylint: disable=abstract-method,too-many-arguments
class SegMlNode(MlNode):
    """ml node class for semantic segmentation"""

    def __init__(
        self,
        projectname: str,
        node_name: str,
        workspace: Union[Path, str],
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
        print_flag: bool = True,
        run_mode: str = "infer",
        debug_level: int = 0,
        full_db_flag: bool = False,
        dump_parent_crops_flag: bool = False,
        all_nodes=None,
        remove_fp: bool = False,
        framework: str = "tensorflow",
    ) -> None:
        super().__init__(
            projectname,
            node_name,
            workspace,
            project_config_path,
            load_model_flag,
            dump_results_flag,
            show_flag,
            git_flag,
            gpu_flag,
            db_stash_flag,
            db_pull_flag,
            wt_stash_flag,
            wt_pull_flag,
            print_flag,
            run_mode,
            debug_level,
            full_db_flag,
            dump_parent_crops_flag,
            all_nodes,
            remove_fp,
            framework,
        )

    def update_crop_json(self, pred_batch, json_crops):
        """update crop json with node predictions"""
        # Loop through prediction  masks
        model_input_h, model_input_w = self.node_config_obj("model_input_HW")
        model_output_h, model_output_w = self.node_config_obj("model_output_HW")
        updated_json_crops = []
        for pred_mask, json_crop in zip(pred_batch, json_crops):
            contours_dict = get_contours_multichannel(pred_mask, classes=list(self.node_config_obj("classes").keys()), hull=self.node_config_obj("hull"), morphology_op=self.node_config_obj("morphology_op"))

            json_crop = cleanup_json(json_crop, self.node_labels)

            # adding contour shapes to crop json
            for classname, contours in contours_dict.items():
                if contours is not None:
                    for cnt in contours:
                        if len(cnt) < 4:
                            continue
                        cnt = cv2lab(cnt)
                        contour = rescale_contour(
                            [cnt],
                            model_output_h,
                            model_output_w,
                            model_input_h,
                            model_input_w,
                        )
                        json_crop_dict = create_shape_dict(
                            label=classname,
                            points=contour,
                        )
                        json_crop["shapes"].append(json_crop_dict)
            updated_json_crops.append(json_crop)
        return updated_json_crops

    def create_train_data(self):
        """create imag and masks for semantic training"""
        train_folder = os.path.join(self.node_dir, "train")
        val_folder = os.path.join(self.node_dir, "val")
        test_folder = os.path.join(self.node_dir, "test")
        train_files_list = get_all_files(train_folder, include_extns=[".json"])
        val_files_list = get_all_files(val_folder, include_extns=[".json"])
        test_files_list = get_all_files(test_folder, include_extns=[".json"])
        files_list = train_files_list + val_files_list + test_files_list
        for json_file in files_list:
            start = time.time()
            dirpath = os.path.dirname(json_file)
            json_dict = read_json(json_file)
            img_name = json_dict["imagePath"]
            img = cv2.imread(os.path.join(dirpath, img_name))
            mask = get_index_image(img, json_dict, classes=self.node_config_obj("classes"))
            mask_folder = os.path.join(os.path.dirname(dirpath), "Masks")
            if not check_folder_exists(mask_folder):
                create_directory_safe(mask_folder)
            mask_path = os.path.join(mask_folder, img_name)
            cv2.imwrite(mask_path, mask)
            # print('time for mask creation', time.time()-start)


if __name__ == "__main__":
    pass

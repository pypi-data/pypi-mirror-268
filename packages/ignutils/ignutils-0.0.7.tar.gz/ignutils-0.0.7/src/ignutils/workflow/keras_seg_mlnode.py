"""Actual mlnode class of seguitls
inheriting seg/mlnode"""

from typing import Optional, Union
import os
from pathlib import Path
import shutil
import cv2
from ignutils.workflow.seg_mlnode import SegMlNode
from ignutils.file_utils import get_all_files, create_directory_safe, check_folder_exists
from ignutils.labelme_utils import get_index_image
from ignutils.json_utils import read_json
from ignutils.img_utils import custom_fog_augmentation
try:
    from keras_segmentation.models.all_models import model_from_name
except ImportError:
    print("keras_segmentation not found")

class KerasSegMlNode(SegMlNode):
    """A machine learning node for segmentation tasks using Keras framework.

    Inherits from SegMlNode, and adds methods for loading, training, testing, and predicting segmentation models 
    using the Keras framework"""

    # pylint: disable=useless-parent-delegation,too-many-arguments
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

    def load_model(self, gpu_flag):
        """To load the model locally.
        if weights exists load weights withour pre trained
        else create model with pretrained imagenet model"""
        weight_exist_flag = False
        self.weights_path = os.path.join(self.weight_dir, "model.h5")
        pre_trained = "imagenet"
        if os.path.isfile(self.weights_path):
            weight_exist_flag = True
        if weight_exist_flag:
            pre_trained = None
        self.model = self.get_model(self.node_config_obj("segmentation_modelname"), pre_trained)
        if weight_exist_flag:
            self.model.load_weights(self.weights_path)
        else:
            print("Model created, weights not found to load")
        # self.model.summary()

    def get_model(self, modelname, pre_trained):
        """Based on the model name the corresponding pre-trained model is downloaded from this function."""

        model = model_from_name[modelname](len(self.node_config_obj("classes").keys()) + 1, input_height=self.node_config_obj("model_input_HW")[0], input_width=self.node_config_obj("model_input_HW")[1], pre_trained=pre_trained)
        return model

    def train(self, epochs=10):
        """Train the deep learning model using the training data created by the `create_train_data` method.
        using keras"""
        train_imgs_folder = os.path.join(self.node_dir, "train", "Imgs")
        train_masks_folder = os.path.join(self.node_dir, "train", "Masks")
        val_imgs_folder = os.path.join(self.node_dir, "val", "Imgs")
        val_masks_folder = os.path.join(self.node_dir, "val", "Masks")
        test_imgs_folder = os.path.join(self.node_dir, "test", "Imgs")
        test_masks_folder = os.path.join(self.node_dir, "test", "Masks")

        if not check_folder_exists(train_masks_folder):
            print("create train data")
            self.create_train_data()
        print("Training Started")
        train_images_count = len(get_all_files(train_imgs_folder, include_type = 'image' ))
        val_images_count = len(get_all_files(val_imgs_folder, include_type = 'image' ))
        train_steps = train_images_count//self.node_config_obj("batch_size")
        val_steps = val_images_count//self.node_config_obj("val_batch_size")
        self.model.train(
            train_images=train_imgs_folder, train_annotations=train_masks_folder, val_images=val_imgs_folder, val_annotations=val_masks_folder,
            checkpoints_path=self.weights_path, epochs=epochs, steps_per_epoch=train_steps, batch_size=self.node_config_obj("batch_size"),
            val_steps_per_epoch= val_steps, val_batch_size=self.node_config_obj("val_batch_size"), validate=True,
            do_augment = self.node_config_obj("augment"), custom_augmentation = custom_fog_augmentation
        )
        print(self.model.evaluate_segmentation(inp_images_dir=test_imgs_folder, annotations_dir=test_masks_folder))

    def test(self, folderpath):
        """Evaluate model on a set of images"""
        image_files = get_all_files(folderpath, include_type='image')
        print(f"testing on {len(image_files)} images")
        for image_file in image_files:
            img = cv2.imread(image_file)
            json = os.path.splitext(image_file)[0] + '.json'
            if not os.path.isfile(json):
                assert f"json file not present for {image_file}"
            json_dict = read_json(json)
            folderpath_annotated = os.path.dirname(folderpath) + "_annotated"
            create_directory_safe(folderpath_annotated)
            mask = get_index_image(img, json_dict, classes=self.node_config_obj("classes"))
            img_name = json_dict["imagePath"]
            mask_path = os.path.join(folderpath_annotated, img_name)
            cv2.imwrite(mask_path, mask)
        print(self.model.evaluate_segmentation(inp_images_dir=folderpath, annotations_dir=folderpath_annotated))
        shutil.rmtree(folderpath_annotated)

    def predict(self, img_batch):
        """image batch for prediciton
        eg:
        pred_batch = self.model.predict(img_batch)
        """
        pred_batch = self.model.predict_multiple(inps=img_batch)
        return pred_batch


if __name__ == "__main__":
    pass

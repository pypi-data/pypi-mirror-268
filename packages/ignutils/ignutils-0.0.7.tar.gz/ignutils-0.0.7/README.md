# ignutils
<div align="center">
  <img src="ignitarium-logo.png">
</div>

[![PyPI version](https://badge.fury.io/py/ignutils.svg)](https://badge.fury.io/py/ignutils)

A python package of reusable, battle tested common modules, mainly related to image processing. Issues and contributions are welcome.

## Install

`python3.8 -m venv venv3.8`\
`source venv3.8/bin/activate`\
`pip3 install --upgrade pip`\
`pip3 install -e ignutils/`

### [ignutils](ignutils)  :heart_eyes_cat: Computer Vision Package

- [x] [Json Utils](ignutils/ignutils/json_utils.py): Utils for reading, writing, comparing json files..

- [x] [Transform Utils](ignutils/ignutils/transform_utils.py) : transform_crop, transform paste, transform_img, transform_contour, expand_box, etc.

![Transform](samples/ppt_images/tansform_utils.jpg)

- [x] [Geom Utils](ignutils/ignutils/geom_utils.py) : Geometric operations using points, lines eg: euclidean, line_intersection, get_nearest_pt on a curve.

- [x] [Contour Utils](ignutils/ignutils/contour_utils.py)  : Resizig, rotation, shifting, union, intersection etc of contours.

![Contour](samples/ppt_images/contour_utils.jpg)

- [x] [Show Utils](ignutils/ignutils/show_utils.py) : Show image and json, handles user keypress, wrapper for imshow ans matplot.

- [x] [MultiProcess](ignutils/ignutils/multi_process_utils.py) : Base class for multiprocess, inherit and overide do_something function.

- [x] [Gpu Utils](cvutils/cvutils/gpu_utils.py) : Get gpu memory free, select device for tensorflow and pytorch, etc

- [x] [Mouse Utils](ignutils/ignutils/mouse_utils.py) : Mouse based ROI selection, contour drawing etc.
  
![Mouse utils](samples/ppt_images/mouse_utils.jpg)

- [x] [Keyboard Utils](cvutils/cvutils/keyboard_utils.py) : Keyboard based utils for selected key recognition.

- [x] [Fisheye Utils](ignutils/ignutils/fisheye_utils.py)  : Handling fisheye distortion and undistortion, cropping from distorted image.

- [x] [Draw Utils](ignutils/ignutils/draw_utils.py)     : Drawing text and polygon on image with params autoselcted.

![Draw Utils](samples/ppt_images/draw_utils.jpg)

- [x] [Clone Utils](ignutils/ignutils/clone_utils.py)

![Clone Utils](samples/ppt_images/sample_clone_utils.jpg)

- [x] [Yaml Utils](ignutils/ignutils/yaml_utils.py) : Read, Write, Custom Format Yaml files.

- [x] [Registration](cvutils/cvutils/registration/)   : Wrapper for registration based on keypoint, ECC, superglue, optical flow etc.

To use **superglue_register**

```
cd src/ignutils/registration/
git clone https://github.com/magicleap/SuperGluePretrainedNetwork
```

- [x] [Video Utils](ignutils/ignutils/video_utils/)    : Getting frames from video , with preprocessing and threading options.

- [x] [Cam Utils](ignutils/ignutils/cam_utils): Getting frames from camera, setting properties of camera.

![Cam Utils](samples/ppt_images/sample_cam_utils.jpg)

- [x] [Config Utils](ignutils/ignutils/config_utils.py): Class to handle config creation for any module with config_path as input.​


- [x] [File Utils](ignutils/ignutils/file_utils.py) : Funcs for handling files.\
Eg: get files by extension, checksum of file etc.

- [x] [TypeHint Utils](ignutils/ignutils/typehint_utils.py) : Typehint for common data structures like contour, image, etc for making functions more readable   

- [x] [Docker Utils](ignutils/ignutils/docker_utils.py): To handle basic docker functionalitys like bringdown_container, bringup_container etc,.

- [x] [Labelme Utils](ignutils/ignutils/labelme_utils.py): Utils for functions like clean up classes, upgrading, writing label json etc., of labelme files.\
Eg: Upgrade all json in a folder: `python -m ignutils.labelme_utils -d json_folder`

- [x] [SSH Utils](ignutils/ignutils/ssh_utils.py): Utils for mounting and unmounting sshfs filesystems

- [x] [Timer Utils](ignutils/ignutils/timer_utils.py): Utils to do tic toc to check time spent
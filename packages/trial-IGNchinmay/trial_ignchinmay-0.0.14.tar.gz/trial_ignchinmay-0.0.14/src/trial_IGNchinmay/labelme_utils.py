"""To convert the labelme dictionary to a json file."""

import argparse
import unittest
from pathlib import Path
from typing import Optional, Union
import numpy as np
import tqdm
from trial_IGNchinmay.json_utils import read_json, write_json
from trial_IGNchinmay.file_utils import get_all_files
from trial_IGNchinmay.draw_utils import draw_polylines


def write_label_json(jsonpath, jsondata: dict, image_path: Optional[Union[Path, str]] = None):
    """Saves label json file after conveting it to labelme suitable json"""
    # saving config to json file for loading later
    if image_path:
        jsondata["imagePath"] = image_path
    jsondata = upgrade_label_json(jsondata)
    write_json(jsonpath, jsondata)


def create_labelme_json():
    """To create a result JSON with shape information and
    image path information, that supports labelme.
    Returns the created json_dict
    """
    json_dict = {}
    json_dict["version"] = "5.0.1"
    json_dict["imageHeight"] = None
    json_dict["imageWidth"] = None
    json_dict["shapes"] = []
    json_dict["imagePath"] = None
    json_dict["imageData"] = None
    json_dict["lineColor"] = [0, 255, 0, 128]
    json_dict["fillColor"] = [255, 0, 0, 128]
    return json_dict


def upgrade_label_json(json_dict):
    """For converting custom json to latest labelme 
    suitable json and returns that dict."""
    json_dict["imageData"] = None
    json_dict["lineColor"] = None  # [0, 255, 0, 128]
    json_dict["fillColor"] = None  # [0, 255, 0, 128]
    shape_list = json_dict["shapes"]
    for shape in shape_list:
        shape["line_color"] = shape.get("line_color", shape.get("color", None))  # put line color else color
        shape["fill_color"] = shape.get("fill_color", None)
    return json_dict


def cleanup_json(json_dict, delete_labels):
    """Removes the labels from the json dictionary given delete_labels."""
    new_cntr_shapes = []
    for cntr_shape in json_dict["shapes"]:
        if cntr_shape["label"] not in delete_labels:
            new_cntr_shapes.append(cntr_shape)
    json_dict["shapes"] = new_cntr_shapes
    return json_dict


def create_shape_dict(label=None, points=None, fill_color=None, shape_type="polygon", line_color=None, overlay_mode=None, fill=False, line_thickness=1):
    """Returns a labelme supported shape dict"""
    if points is None:
        points = []

    shape_dict = {}
    shape_dict["points"] = points
    shape_dict["label"] = label
    shape_dict["line_color"] = line_color
    shape_dict["fill_color"] = fill_color
    shape_dict["shape_type"] = shape_type
    shape_dict["color"] = line_color
    shape_dict["overlay_mode"] = overlay_mode
    # shape_dict["node_name"] = node_name
    shape_dict["fill"] = fill
    shape_dict["line_thickness"] = line_thickness
    shape_dict["flags"] = {}
    return shape_dict


def upgrade_label_dir(json_folder):
    """upgrade label json to latest labelme type"""
    json_files = get_all_files(json_folder, include_extns=".json")
    for json_file in tqdm.tqdm(json_files):
        json_dict = read_json(json_file)
        new_json_dict = upgrade_label_json(json_dict)
        write_json(json_file, new_json_dict)
    print(f"upgrade_label_dir- {json_folder} done")
    return True


def get_index_image(image, json_dict, classes=(())):
    """Returns mask image based on classes (co-labels included)"""
    shapes = json_dict["shapes"]
    canvas = np.zeros_like(image)
    seg_mask = np.zeros_like(image)
    for index, classname in enumerate(classes):
        co_labels = classes[classname]["co_labels"]
        for shape in shapes:
            if shape["label"] in co_labels:
                points = shape["points"]
                color_draw = classes[classname]["color"]
                canvas = draw_polylines(canvas, points, fill=True, color=color_draw)
                seg_mask[np.where((canvas == color_draw).all(axis=2))] = [int(index + 1), int(index + 1), int(index + 1)]
    return seg_mask

def get_label_contours(json_dict, label_list):
    """Returns list of contours with labelnames in label_list given"""
    contours_list = []
    shapes = json_dict['shapes']
    for shape in shapes:
        if shape['label'] in label_list:
            contours_list.append(shape['points'])
    return contours_list

def get_label_count(json_dict, label_list):
    """Get label count in json"""
    shapes = json_dict['shapes']
    label_count = 0
    for shape in shapes:
        if shape['label'] in label_list:
            label_count+=1
    return label_count


class TestLabemeUtils(unittest.TestCase):
    """Test method"""

    @classmethod
    def setUpClass(cls):
        # cls.json_folder_ = "tmp"
        cls.json_folder_ = "samples/json_upgrade_test"

    @classmethod
    def tearDownClass(cls):
        print("teardown")

    def test_upgrade_label_dir(self, json_folder=None):
        """test upgrade_label_json dir"""
        if json_folder:
            self.json_folder_ = json_folder
        upgrade_label_dir(self.json_folder_)
        json_files = get_all_files(self.json_folder_, include_extns=".json")
        for json_file in json_files:
            json_dict = read_json(json_file)
            assert json_dict["imageData"] is None

def main():
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        default="samples/tmp",
        help="json folder to be cleaned up",
    )
    args = parser.parse_args()
    json_folder = args.directory

    test_ = TestLabemeUtils()
    test_.setUpClass()
    test_.test_upgrade_label_dir(json_folder)

if __name__ == "__main__":
    main()

# python -m trial_IGNchinmay.labelme_utils

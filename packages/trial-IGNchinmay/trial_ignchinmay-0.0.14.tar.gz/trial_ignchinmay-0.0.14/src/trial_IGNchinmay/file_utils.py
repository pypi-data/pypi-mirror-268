# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : file_utils.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To hande basic operations such as reading and writing of files and directories."""

import hashlib
import os
import os.path as osp
import shutil
import unittest
import cv2
import numpy as np
import trial_IGNchinmay as icv


def get_all_files(
    rootpath,
    include_type=None,
    include_extns=(),
    exclude_extns=(),
    only_basename=False,
    only_relative_path=False,
    exclude_folders=(".git", ".lock", "__pycache__"),
    checksum_flag = False,
    checksum_overwrite = False,
    checksum_folder = None
):
    """Get all files given in rootpath. Give include either type or extns.
    Args:
        include_type: 'image','video','json'
        include_extns: ['.jpg', '.json', '.MD', etc]
        exclude_extns: ['.jpg', '.json', '.MD', etc]
    Returns:
        a list of file paths with file extention (if specified)
    """
    assert not (len(include_extns) and include_type), "Either include type or include_extns only allowed"
    all_files = []
    if checksum_flag:
        root_path = make_file_path(rootpath)
        checksum_path = os.path.join(os.path.join("tmp", root_path),checksum_folder, "checksum.json")
        if os.path.isfile(checksum_path):
            checksum_dict = icv.json_utils.read_json(checksum_path)
        else:
            if not check_folder_exists(os.path.join("tmp", root_path, checksum_folder)):
                create_directory_safe(os.path.join("tmp", root_path, checksum_folder))
            checksum_dict = {}
    for root, _, files in os.walk(rootpath):
        root_split_list = root.split(os.sep)
        skip_flag = False
        for item in root_split_list:
            if item in exclude_folders:
                skip_flag = True
        if skip_flag:
            continue
        for f in files:
            basename_no_ext, extn = osp.splitext(f)
            if extn in exclude_extns:
                continue
            if include_extns and extn not in include_extns:
                continue
            if include_type == "image":
                if not is_image_file(f):
                    continue
            elif include_type == "video":
                if not is_video_file(f):
                    continue
            full_p = osp.join(root, f)
            if only_relative_path:  # to get relative path with respect to input path
                full_p = full_p[len(rootpath) + 1 :]
            # if osp.isfile(full_p):
            if only_basename:
                all_files.append(osp.join(root, basename_no_ext))
            else:
                all_files.append(full_p)
            if checksum_flag and not checksum_overwrite:
                checksum = get_checksum(full_p)
                checksum_dict[full_p] = checksum
                if os.path.isfile(checksum_path) and full_p in checksum_dict:
                    if checksum_dict[full_p] == checksum:
                        if only_basename:
                            all_files.remove(osp.join(root, basename_no_ext))
                        else:
                            all_files.remove(full_p)
    if checksum_flag and (checksum_overwrite or (not os.path.isfile(checksum_path))):
        icv.json_utils.write_json(checksum_path, checksum_dict)

    return all_files


def change_extn(file_path, extn):
    """Change extension as given extn
    Args:
        file_path : relative or full file path
        extn : extension, eg: .json, .png
    Returns:
        File path with changed extension
    """
    assert extn[0] == ".", "extn should start with ."
    basename_no_ext, _ = osp.splitext(file_path)
    new_file = basename_no_ext + extn
    return new_file

def get_checksum(filename):
    """Calculate the MD5 checksum of a given file."""
    md5_hash = hashlib.md5()

    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5_hash.update(chunk)

    return md5_hash.hexdigest()


# def get_checksum_(file_path):
#     """Calculate the MD5 checksum of a given file."""
#     if osp.isfile(file_path):
#         return hashlib.md5(open(file_path, "rb").read()).hexdigest()
#     return None


def is_image_file(filenam):
    """Returns True if its extension is one of image extensions."""
    if os.path.splitext(filenam)[1].lower() in [".jpg", ".png", ".jpeg", ".tiff", ".bpm"]:
        return True
    return False


def is_json_file(filenam):
    """Returns True if the extension is json file"""
    if os.path.splitext(filenam)[1].lower() in [".json"]:
        return True
    return False


def is_video_file(filenam):
    """Returns True if its extension is one of video extensions."""
    if os.path.splitext(filenam)[1].lower() in [".mov", ".avi", ".mp4", ".mpeg"]:
        return True
    return False


def is_video(filepath):
    """Returns True if the video file can be opened using cv2."""
    cap = cv2.VideoCapture(filepath)
    if not cap.isOpened():
        return False
    return True

def find_file(name, path):
    """
    To find specified file in specified root directory
    Args:
        name: filename which needs to be found
        path: path of root directory
    Returns:
        Path of the file if found
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

def make_file_path(file_path, source_path=None, dst_path=None, ext=None):
    """
    Split the file_path using source_path and combine the file_name with directories.
    Args:
        file_path: full path of input fle
        source_path: source folder or root folder of file (path after this will be added to filename)
        dst_path: folder to which file is to be written
        ext: extention of file, if None, filename without extention
    Returns:
        file path with relative path flattened with delimeter --
    """
    path_no_ext = os.path.splitext(file_path)[0]  # path_with_no_ext
    if source_path:
        path_no_ext = path_no_ext.split(source_path)[-1]  # relative file path
    dir_list = path_no_ext.split(os.sep)
    temp_path = os.path.join(*dir_list)
    file_path_no_ext = temp_path.replace(os.sep, "--")  # file_name_with no extension
    if ext:
        file_path = file_path_no_ext + ext
    else:
        file_path = file_path_no_ext
    if dst_path:
        file_path = os.path.join(dst_path, file_path)
    return file_path


def file_names_to_path(files_name_list: list) -> list:
    """Returns converted file names to path"""
    name_path_list = []
    for f_name in files_name_list:
        file_name = osp.splitext(f_name)[0]
        split_list_no_shape_index = file_name.split("--")[:-1]
        name_path = osp.join(*split_list_no_shape_index)
        name_path_list.append(name_path)
    return name_path_list


def get_file_name(filepath):
    """To get only the filename without extenstion from path"""
    return osp.splitext(osp.basename(filepath))[0]


def walkdir(folder, exclude_folders=(".git"), exclude_extns=()):
    """Walk through every files in a directory"""
    for dirpath, dirs, files in os.walk(folder):
        skip = False
        for ex_folder in exclude_folders:
            if ex_folder in dirpath:
                skip = True
                break
        if skip:
            continue
        for filename in files:
            file_extn = osp.splitext(filename)[-1]
            if file_extn in exclude_extns:
                continue
            yield os.path.abspath(os.path.join(dirpath, filename))


def create_directory_safe(direc, verbose=False):
    """Creates directory."""
    if not os.path.isdir(direc):
        os.makedirs(direc, exist_ok=True)
        if verbose:
            print("Created:", direc)
    else:
        if verbose:
            print("Existing:", direc)
    return True


def create_directory_fresh(direc):
    """Creates a fresh directory, deletes and creates if it exists already"""
    remove_directory(direc)
    os.makedirs(direc)
    print("Deleted and created directory:", direc)
    return True


def remove_directory(direc):
    """Removes directory."""
    if os.path.exists(direc):
        shutil.rmtree(direc)


def check_folder_exists(dir_name):
    """Returns True if folder exists."""
    return not remove_if_empty(dir_name)


def check_folder_exists_exclude_git(path):
    """Returns true if folder exists and returns false if it is empty
    or if only git and readme files are present"""
    if os.path.exists(path) and os.path.isdir(path):
        if [f for f in os.listdir(path) if (not f.startswith(".") and not f.endswith(".md"))] == []:
            return False
        return True
    return False


def remove_if_empty(dir_name):
    """Returns True if folder doesn't exists or folder empty (Deletes empty folder)"""
    if os.path.exists(dir_name) and os.path.isdir(dir_name):
        dir_list = os.listdir(dir_name)
        if not dir_list or (len(dir_list) == 1 and ".git" in dir_list):
            print(f"Directory {dir_name} is empty, deleting")
            shutil.rmtree(dir_name)
            return True
        return False
    # print("Given Directory {} does not exists".format(dirName))
    return True


def copyfilesimple(src, dest):
    """Given a source file copied to destination directory."""
    if not os.path.exists(dest):
        create_directory_safe(dest)
    shutil.copy(src, dest)


# @lru_cache(maxsize=300)
def get_img_batch(img_path_list):
    """Returns image batch for image path list"""
    img_batch = []
    for img_path in img_path_list:
        img = cv2.imread(img_path)
        img_batch.append(img)
    return img_batch


def update_dst_files(src_path, dst_path):
    """Update dst files based on src files"""
    src_json_files = get_all_files(src_path, include_extns=[".json"], only_relative_path=True)
    dst_json_files = get_all_files(dst_path, include_extns=[".json"], only_relative_path=True)
    src_json_base_names = [os.path.basename(src_json_file) for src_json_file in src_json_files]
    u, i = np.unique(src_json_base_names, return_inverse=True)
    print("duplicate", u[np.bincount(i) > 1])
    assert len(src_json_files) > 0 and len(dst_json_files) > 0, "Src or dst is not valid"
    assert len(src_json_files) == len(src_json_base_names), "Unique count not matching"
    for dst_json_path in dst_json_files:
        dst_json_base_name = os.path.basename(dst_json_path)
        if dst_json_base_name in src_json_base_names:
            src_index = src_json_base_names.index(dst_json_base_name)
            src_file = os.path.join(src_path, src_json_files[src_index])
            dst_file = os.path.join(dst_path, dst_json_path)
            print(f"copying {src_file} to {dst_file}")
            shutil.copy(src_file, dst_file)


def convert_to_jpg(src_path, dst_path, quality=100):
    """read image from the source path and write image as a jpg in the dst path"""
    img = cv2.imread(src_path)
    cv2.imwrite(dst_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])


def convert_all_matching(src_path, src_extn, dst_extn):
    """Converts image file with the src_extn (Eg. png) to dst_extn (Eg. jpg)
    in the same location and removes the files with src_path. Currently supports
    conversion to jpg/jpeg/JPG/JPEG files"""
    src_files = get_all_files(src_path, include_extns=[src_extn], only_relative_path=True)
    for src_file in src_files:
        src_file_path = os.path.join(src_path, src_file)
        dst_file_path = os.path.join(src_path, src_file.replace(src_extn, dst_extn))
        print(f"converting {src_file_path} to {dst_file_path}")
        if dst_extn in [".jpg", ".jpeg", ".JPG", ".JPEG"]:
            convert_to_jpg(src_file_path, dst_file_path)
            os.remove(src_file_path)


def read_file(filename="readme.txt"):
    """Reads from the provided text file and
    Returns a list of text lines."""
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    return lines


def write_file(txt="Hello", filename="readme.txt"):
    """Writes the text (txt) to the file provided"""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(txt)


class TestFileUtils(unittest.TestCase):
    """test_file_utils_options"""

    def test_get_all_file(self):
        """test get all files"""
        files = get_all_files(
            rootpath="notebooks",
            include_type=None,
            include_extns=(".ipynb"),
            exclude_extns=(),
            only_basename=False,
            only_relative_path=False,
            exclude_folders=(".git", ".lock", "__pycache__"),
            checksum_flag=False
        )
        assert len(files) == 1, f"notebooks folder is expected to have 3 files, got {len(files)}"

    def test_convert_all_matching(self):
        """test convert all matching"""
        src_path = "/home/skycam/aTYQI/ign_utils/trial_IGNchinmay/trial_IGNchinmay/registration/kitti05/image_1"
        src_extn = ".png"
        dst_extn = ".jpg"
        convert_all_matching(src_path, src_extn, dst_extn)
        files = get_all_files(
            rootpath=src_path,
            include_type=None,
            include_extns=src_extn,
            exclude_extns=(),
            only_basename=False,
            only_relative_path=False,
            exclude_folders=(".git", ".lock", "__pycache__"),
        )
        assert len(files) == 0, f"{src_path} folder is expected to have 0 png files, got {len(files)}"


if __name__ == "__main__":
    test_obj = TestFileUtils()
    test_obj.test_get_all_file()
    test_obj.test_convert_all_matching()

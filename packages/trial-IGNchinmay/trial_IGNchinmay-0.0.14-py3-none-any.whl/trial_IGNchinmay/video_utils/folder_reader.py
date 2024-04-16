"""reads image frames from a folder containing image files with extensions .jpg, .png, .jpeg, .tiff, .bmp.
The class can be used to read individual frames and the total number of frames in the folder"""
import base64
import os
import re
import unittest
import cv2

from trial_IGNchinmay.draw_utils import print_colored
from trial_IGNchinmay.show_utils import show

class FolderReader:
    """concrete class 2"""

    def __init__(self, folder_path="video", encode_mode=False):
        self.total_frame_count = 0
        self.image_names = []
        self.image_paths = []
        self.frame_num = 0
        self.folder_path = folder_path
        self.encode_mode = encode_mode
        self.len = 0
        assert os.path.isdir(folder_path), "folder_path doesnt exist"
        for root, _, files in os.walk(self.folder_path):
            for file_ in files:
                if os.path.splitext(file_)[1].lower() in [
                    ".jpg",
                    ".png",
                    ".jpeg",
                    ".tiff",
                    ".bpm",
                ]:
                    self.total_frame_count += 1
                    self.full_p = os.path.join(root, file_)
                    self.img_name = os.path.splitext(os.path.basename(self.full_p))[0]
                    self.image_names.append(self.img_name)
                    self.image_paths.append(self.full_p)
        self.image_paths.sort(key=lambda f: int(re.sub(r"\D", "", f)))
        self.len = len(self.image_paths)
        img = cv2.imread(self.image_paths[0])
        self.frame_width, self.frame_height = img.shape[1], img.shape[0]

    def get_total_frames(self):
        """returns the total number of frames in the data"""
        return self.len

    def set_framenum(self, frame_num):
        """Set Video to a specific frame number

        Args:
            frame_num (int): required frame num

        """
        if frame_num > self.total_frame_count:
            print("*" * 50)
            print(f"{frame_num} exceeded total frame count {self.total_frame_count}")
            print("*" * 50)
        if frame_num > self.total_frame_count or frame_num < 0:
            print_colored("[!] Error! frame_num > self.total_frame_count or frame_num<0", "red")
        self.frame_num = frame_num
        return True

    def next_frame(self):
        """Retrieves the next frame of data in either base64 encoded string format or numpy array format"""
        self.frame_num += 1
        if self.frame_num <= self.total_frame_count:
            imgpath = self.image_paths[self.frame_num - 1]
            filename = os.path.splitext(os.path.basename(imgpath))[0]
            if self.encode_mode is True:
                with open(imgpath, "rb") as img:
                    img_bytes = img.read()
                img_bytes = base64.b64encode(img_bytes).decode("ascii")
                return img_bytes, self.frame_num - 1, filename
            img_array = cv2.imread(imgpath)
            return img_array, self.frame_num - 1, filename
        return None, None, None

class TestFolderReader(unittest.TestCase):
    """Test methods"""

    def test_folder_reader(self, show_img=False):
        """Testing folder reader class using sample images"""
        sample_imgs_path = os.path.join("samples", "video_utils_test")
        reader_obj = FolderReader(sample_imgs_path)
        res_no = 0
        while True:
            frame, frame_num, name = reader_obj.next_frame()
            if frame is None:
                break
            res_no += 1
            if show_img:
                show(frame, "sample", time=0)
        assert res_no == 5, "Folder reader test failed"

if __name__ == "__main__":
    test_obj = TestFolderReader()
    test_obj.test_folder_reader()

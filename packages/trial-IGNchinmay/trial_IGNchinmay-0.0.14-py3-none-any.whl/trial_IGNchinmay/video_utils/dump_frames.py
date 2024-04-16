"""To dump frames from a given video pair."""
import os
import os.path as osp
import unittest
from shutil import rmtree
import cv2

from trial_IGNchinmay.video_utils.video_reader import VideoReader
from trial_IGNchinmay.mouse_utils import MousePts
from trial_IGNchinmay.transform_utils import transform_crop
from trial_IGNchinmay.file_utils import get_all_files

def dump_video_frames(video_path: str, dump_path: str, start_framenum: int = 0, frame_skip: int = 0, dump_frame_cnt=None, crop_frame=False) -> None:
    """Method to dump frames of video given the video path and the dumm path. Dump path is deleted if it exists.

    Args:
        video_path (str): Path of input video.
        dump_path (str): Path for dumping the frames of video.
        start_framenum (int, optional): Starting frame number for dumping. Defaults to 0.
        frame_skip (int, optional): Frame skip for dumping. Defaults to 0.
    """
    if osp.isfile(video_path) is False:
        raise FileNotFoundError(f"Video path not found: {video_path}")
    if osp.isdir(dump_path):
        print(f"{dump_path} already exists. Deleting...")
        rmtree(dump_path)
    os.makedirs(dump_path)

    print(f"Reading video from {video_path}")
    reader = VideoReader(video_path)
    total_frames = reader.get_total_frames()
    print(f"Total frame count: {total_frames}")
    print(f"Setting start frame num as {start_framenum}")
    reader.set_framenum(start_framenum)
    frame_no = start_framenum
    dump_count = 0
    fixed_roi = None

    for i in range(total_frames):
        org_frame, processed_frame, frame_num, trans_mat, _ = reader.get_frame(frame_no)
        frame_no += 1
        if org_frame is None or i == dump_frame_cnt:
            break

        if crop_frame and fixed_roi is None:
            mouse_obj = MousePts()
            fixed_roi = mouse_obj.select_roi(org_frame)
            print("ROI: ", fixed_roi)

        if crop_frame:
            org_frame, _, __, _ = transform_crop(image=org_frame, crop_cntr=fixed_roi)

        if i % (frame_skip + 1) == 0:
            cv2.imwrite(osp.join(dump_path, str(frame_num) + ".jpg"), org_frame)
            dump_count += 1

    print(f"Dump path: {dump_path}")
    print(f"Number of dumped images: {dump_count}")


class TestDumpFrames(unittest.TestCase):
    """Test methods"""

    def test_dump_frames(self):
        """Testing dump frames from video"""
        video_path = os.path.join("samples", "video_utils_test", "sample.mp4")
        dump_path = os.path.join("samples", "video_utils_test", "results")
        dump_video_frames(video_path, dump_path, start_framenum=0, dump_frame_cnt=5, crop_frame=False)
        dumped_img_paths = get_all_files(dump_path)
        dumped_img = cv2.imread(dumped_img_paths[0])
        assert dumped_img.shape is not None, "Image dump failed"

if __name__ == "__main__":
    test_obj = TestDumpFrames()
    test_obj.test_dump_frames()

# --------------------------------------------------------------------------
#                         Copyright © by

#           Ignitarium Technology Solutions Pvt. Ltd.

#                         All rights reserved.


#  This file contains confidential information that is proprietary to

#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,

#  disclosure or reproduction of this file in part or whole is strictly

#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : video_writer.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""Demo file to write a video in mp4 format."""

import os
import unittest
import subprocess as sp
import cv2
import numpy as np

from trial_IGNchinmay.file_utils import get_all_files
from trial_IGNchinmay.video_utils.video_reader import VideoReader


class VideoWriter:
    """Class for writing frames to video.
    IMPORTANT: Please make sure you call release() after done writing frames.

    Args:
        outfile (str): Path to the file.
        fps (int): Frames per second required for output video.
        fourcc: OpenCV fourcc method.
        use_ffmpeg: Use ffmpeg instead of OpenCV
    """

    def __init__(self, outfile: str, fps: int, fourcc=cv2.VideoWriter_fourcc("m", "p", "4", "v"), use_ffmpeg=False) -> None:
        self.outfile = outfile
        self.fps = fps
        self.fourcc = fourcc
        self.writer = None
        self.command = None

        self.use_ffmpeg = use_ffmpeg
        print("Video Writer initialized..")

    def write_frame(self, frame: np.ndarray) -> None:
        """write frame"""
        if self.writer is None:
            height, width = frame.shape[:2]
            if self.use_ffmpeg is False:
                self.writer = cv2.VideoWriter(self.outfile, self.fourcc, self.fps, (width, height))
            else:
                self.command = [
                    "ffmpeg",
                    "-y",  # (optional) overwrite output file if it exists
                    "-f",
                    "rawvideo",
                    # '-vcodec','rawvideo',
                    "-s",
                    f"{width}x{height}",  # size of one frame
                    "-pix_fmt",
                    "bgr24",
                    "-r",
                    f"{self.fps}",  # frames per second
                    "-i",
                    "-",  # The imput comes from a pipe
                    "-an",  # Tells FFMPEG not to expect any audio
                    "-vcodec",
                    "mpeg4",
                    f"{self.outfile}",
                    "-threads",
                    "8",
                    "-metadata",
                    "test=metadata"
                ]
                self.writer = sp.Popen(self.command, stdin=sp.PIPE, stderr=sp.PIPE) # pylint: disable=R1732

        if self.use_ffmpeg is False:
            self.writer.write(frame)
        else:
            self.writer.stdin.write(frame.tobytes())

    def release(self):
        """release writer object"""
        if self.use_ffmpeg:
            self.writer.stdin.close()
            self.writer.stderr.close()
        else:
            self.writer.release()
        print("writer obj released")

    def __del__(self):
        self.release()

class TestVideoWriter(unittest.TestCase):
    """Test methods"""

    def test_video_writer(self):
        """Testing video writer class using sample images"""
        sample_imgs_path = os.path.join("samples", "video_utils_test", "results")
        write_path = os.path.join("samples", "video_utils_test", "results", "sample.mp4")
        use_ffmpeg = False
        fps_ = 25
        writer_obj = VideoWriter(write_path, fps_, use_ffmpeg=use_ffmpeg)
        sample_imgs_path = get_all_files(sample_imgs_path, exclude_extns=".mp4")
        for img_path in sample_imgs_path:
            frame = cv2.imread(img_path)
            writer_obj.write_frame(frame)
        writer_obj.release()
        reader_obj = VideoReader(write_path)
        total_frames = reader_obj.get_total_frames()
        assert total_frames == 11, "Video Writer test failed"

if __name__ == "__main__":
    test_obj = TestVideoWriter()
    test_obj.test_video_writer()

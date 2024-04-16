# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : video_sync.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To establish the synchronization between left and right video streams."""
import argparse
import os
import cv2
import numpy as np

from trial_IGNchinmay.draw_utils import print_colored, put_text
from trial_IGNchinmay.video_utils.play_video import play
from trial_IGNchinmay.show_utils import show


class PlayerWrapper:
    """Calling video player inside multi process"""

    def __init__(self, in_args):
        self.args = in_args
        self.frame_num = None
        self.curr_frame = None
        self.autosync = False
        self.toggle = False
        self.cap = cv2.VideoCapture(self.args.get("filepath"))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def play_video(self, start_frame):
        """Calling play video function"""
        args = self.args
        res_dict = play(args.get("filepath"), start_frame, window_name=args.get("window_name"), window_w=args.get("window_w"), window_h=args.get("window_h"), pos_x=args.get("pos_x"), pos_y=args.get("pos_y"), esc_txt="Save & Close Window")
        start_frame = res_dict.get("frame_num")
        self.frame_num = start_frame
        self.curr_frame = res_dict.get("current_frame")
        self.autosync = res_dict.get("autosync")
        self.toggle = res_dict.get("toggle")

    def get_frame_from_video(self, frame_no):
        """Get specific frame from video"""
        if frame_no is not None:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no - 1)
            _, frame = self.cap.read()
        else:
            frame = None

        return frame


class VideoSync:
    """Sync two Videos by poping two seperate windows"""

    def __init__(self, left_video_path, right_video_path, left_data_path, right_data_path, left_start_frame=None, right_start_frame=None, window_width=1000, window_height=1000):
        self.left_video_path = left_video_path
        self.right_video_path = right_video_path
        self.left_data_path = left_data_path
        self.right_data_path = right_data_path
        self.left_start_frame = left_start_frame
        self.right_start_frame = right_start_frame
        self.window_width = window_width
        self.window_height = window_height
        self.left_start_frame_path = os.path.join(left_data_path, "start_frame_left.txt")
        self.right_start_frame_path = os.path.join(right_data_path, "start_frame_right.txt")
        if self.left_start_frame is None:
            self.left_start_frame = 0
        if self.right_start_frame is None:
            self.right_start_frame = 0

        self.args_l = {
            "filepath": self.left_video_path,
            "dst_path": self.left_start_frame_path,
            "window_name": "Left Sync Adjust",
            "window_w": self.window_width,
            "window_h": self.window_height,
            "pos_x": 100,
            "pos_y": 100,
        }
        self.left_player = PlayerWrapper(self.args_l)

        self.args_r = {
            "filepath": self.right_video_path,
            "dst_path": self.right_start_frame_path,
            "window_name": "Right Sync Adjust",
            "window_w": self.window_width,
            "window_h": self.window_height,
            "pos_x": 1100,
            "pos_y": 100,
        }
        self.right_player = PlayerWrapper(self.args_r)

    def play_left(self, initial_sync=False):
        """Sync window for left video"""
        if self.right_player.frame_num is not None and self.right_player.curr_frame is not None:
            right_selected_frame = self.get_refer_frame(self.right_player.curr_frame, self.right_player.frame_num)
        else:
            right_selected_frame = self.get_refer_frame(self.right_player.get_frame_from_video(self.right_start_frame), self.right_start_frame)

        if right_selected_frame is not None:
            show(img=right_selected_frame, win="Right Sync Reference", time=30, x=1100, y=100, width=1000, height=1000)

        self.left_player.play_video(self.left_start_frame)
        left_offset = None
        if self.left_player.frame_num is not None:
            left_offset = self.left_player.frame_num - self.left_start_frame

        if initial_sync:
            if left_offset is not None:
                right_offset = self.right_start_frame + left_offset
                if right_offset >= self.right_player.total_frames or right_offset < 0:
                    print_colored("[!] Warning, Offset frame count exceeded available limits. Setting right start frame no to initial", "yellow")
                else:
                    self.right_start_frame = right_offset

        self.left_start_frame = self.left_player.frame_num
        self.save_start_frames(self.left_start_frame, self.right_start_frame)

        return self.left_player.autosync, self.left_player.toggle

    def play_right(self):
        """Sync window for right video"""
        if self.left_player.frame_num is not None and self.left_player.curr_frame is not None:
            left_selected_frame = self.get_refer_frame(self.left_player.curr_frame, self.left_player.frame_num)
        else:
            left_selected_frame = self.get_refer_frame(self.right_player.get_frame_from_video(self.left_start_frame), self.left_start_frame)

        if left_selected_frame is not None:
            show(img=left_selected_frame, win="Left Sync Reference", time=30, x=100, y=100, width=1000, height=1000)

        self.right_player.play_video(self.right_start_frame)
        self.left_start_frame, self.right_start_frame = self.left_player.frame_num, self.right_player.frame_num
        self.save_start_frames(self.left_start_frame, self.right_start_frame)

        return self.right_player.autosync, self.right_player.toggle

    def get_refer_frame(self, frame_l, frame_num):
        """Using this function we can put the roi and frame number on the left reffrence frame"""
        reffrence_frame = frame_l
        h, w = reffrence_frame.shape[:2]
        font_scale = int(h / 1000)
        thickness = max(1, int(h / 400))
        reffrence_frame = put_text(
            str("Frame Num: " + str(frame_num)),
            reffrence_frame,
            w - 500,
            150,
            color=[0, 255, 0],
            font_scale=font_scale,
            thickness=thickness,
            font=cv2.FONT_HERSHEY_COMPLEX,
            draw_bg=True,
        )
        return reffrence_frame

    def load_start_frame(self, file_path):
        """Load the start frame from the file"""
        return np.loadtxt(file_path).astype(int).tolist()

    def save_start_frames(self, left_frame_no, right_frame_no):
        """Save start frames"""
        print(f"Saving left start frame: {left_frame_no} to {self.left_start_frame_path}")
        np.savetxt(self.left_start_frame_path, np.array([left_frame_no]).astype(int), fmt="%i")
        print(f"Saving right start frame: {right_frame_no} to {self.right_start_frame_path}")
        np.savetxt(self.right_start_frame_path, np.array([right_frame_no]).astype(int), fmt="%i")


if __name__ == "__main__":
    LEFT_DATA_PATH = "Left"
    RIGHT_DATA_PATH = "Right"

    parser = argparse.ArgumentParser()
    parser.add_argument("-f1", "--filepath1", type=str, default=None, help="input video file path")
    parser.add_argument("-f2", "--filepath2", type=str, default=None, help="input video file path")

    args = parser.parse_args()

    left_video_path_ = args.filepath1
    right_video_path_ = args.filepath2
    os.makedirs(LEFT_DATA_PATH, exist_ok=True)
    os.makedirs(RIGHT_DATA_PATH, exist_ok=True)
    VideoSync(left_video_path_, right_video_path_, LEFT_DATA_PATH, RIGHT_DATA_PATH)

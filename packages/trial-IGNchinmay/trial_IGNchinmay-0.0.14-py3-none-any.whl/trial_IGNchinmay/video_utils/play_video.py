"""To read a video file and to display the video frame by frame."""

import argparse
import os

import cv2

from trial_IGNchinmay.draw_utils import put_text, put_texts
from trial_IGNchinmay.show_utils import set_window_property, show

PATH = os.path.dirname(os.path.abspath(__file__))


def play(video_path, start_frame=None, duration=None, window_name="Window", window_h=None, window_w=None, pos_x=None, pos_y=None, esc_txt="Close Window"):
    """Play a video file
    Usage Example: python -m trial_IGNchinmay.video_utils.play_video -f 2.mp4
    """
    cap = cv2.VideoCapture(video_path)

    fr = 0
    valid_fr = 0
    if start_frame is not None:
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        fr = start_frame
    if duration is not None:
        cap.set(cv2.CAP_PROP_POS_MSEC, duration)
    if pos_x is not None and pos_y is not None:
        set_window_property(window_name, pos_x, pos_y, window_w, window_h)
    framecopy = None
    refer_copy = None
    frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Total_frames: ", frames_count, "fps: ", fps)
    k = 1
    autosync = False
    toggle = False
    while cap.isOpened():
        if k != -1:
            ret, frame = cap.read()

        if ret:
            valid_fr = fr
            framecopy = frame.copy()
            refer_copy = frame.copy()
            put_text(f"Frame {fr}", framecopy, framecopy.shape[1] - 30, 100, color=(0, 255, 255), thickness=3, font_scale=2, draw_bg=True, auto_align_h=True, auto_align_v=True)
            put_texts(img=framecopy, test_tuple_list=["****Active Window****", "t - Toggle left/right", "s - AutoSync", "n - Next Frame", "p - Previous Frame", f"Esc - {esc_txt}"], v_space=100)

        if framecopy is not None:
            k = show(framecopy, time=0, win=window_name)
            if k == ord("n"):
                if ret:
                    fr += 1
                else:
                    fr = valid_fr

            elif k == ord("p"):
                fr -= 1
                fr = max(0, fr)
                cap.set(cv2.CAP_PROP_POS_FRAMES, fr)

            elif k == ord("s"):
                autosync = True
                toggle = False
                break

            elif k == ord("t"):
                autosync = False
                toggle = True
                break

            elif k == 27:
                autosync = False
                toggle = False
                break

            else:
                k = -1

    cap.release()
    cv2.destroyAllWindows()

    result_dict = {"frame_num": fr, "current_frame": refer_copy, "autosync": autosync, "toggle": toggle}

    return result_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filepath", type=str, default=os.path.join(PATH, "sample.mp4"), help="input video file path")
    parser.add_argument(
        "-sf",
        "--start_frame",
        type=int,
        default=None,
        help="start frame number for video",
    )
    parser.add_argument(
        "-dur",
        "--duration",
        type=float,
        default=None,
        help="Duration for which the application to be run",
    )

    args = parser.parse_args()

    play(args.filepath, args.start_frame, args.duration)

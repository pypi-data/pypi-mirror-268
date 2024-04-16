# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : show_utils.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------

"""To do basic image processing operations like generating masked images, fuseing, blending, concatination, flickering of images and to show the results of these operations."""

import os
from typing import List
import unittest
from threading import Thread
import time as T
from queue import Queue
import numpy as np
import cv2
import matplotlib.pyplot as plt
from pylab import imshow, show, get_cmap
from numpy import random
from trial_IGNchinmay.file_utils import get_all_files
from trial_IGNchinmay.multi_process_utils import BaseProcess
from trial_IGNchinmay.typehint_utils import CntrL
from trial_IGNchinmay.draw_utils import draw_cntrs


def show(img, win="img", time=1, destroy=False, k=-1, window_normal=True, x=None, y=None, width=None, height=None, clip=False, resize_w=None, resize_h=None):
    """show image in a named window using cv2
    img: Input Image
    win: Display window name, defaults to "img"
    time: Display window time, defaults to 30 milliseconds
    destroy: To destroy window at end of show, defaults to False
    k: To pass any user key press, defaults to -1
    window_normal: Type of window to display, defaults to True
    """
    # cv2.startWindowThread()
    if isinstance(img, str):
        img = cv2.imread(img)
    if clip:
        img = np.clip(img, 0, 255)
        img = img.astype("uint8")
    if window_normal:
        cv2.namedWindow(win, cv2.WINDOW_GUI_NORMAL)
    if height is not None and width is not None:
        cv2.resizeWindow(win, width, height)
    if x is not None and y is not None:
        cv2.moveWindow(win, x, y)
    if resize_h and resize_w:
        cv2.resizeWindow(win, resize_w, resize_h)
    # cv2.moveWindow(win, 1366, 768)
    cv2.imshow(win, img)
    if k == -1:
        k = cv2.waitKey(time)
    if k == ord("q"):
        print("[!] User pressed Q, Application Quiting!")
        quit()
    if destroy:
        cv2.destroyWindow(win)
    return k


def set_window_property(win, x, y, wd, ht):
    """set window"""
    cv2.namedWindow(win, cv2.WINDOW_GUI_NORMAL)
    cv2.resizeWindow(win, wd, ht)
    cv2.moveWindow(win, x, y)


def destroy_all_windows():
    """Destroy all open windows"""
    cv2.destroyAllWindows()


def masked_add(fg_image, bg_image, mask, alpha=0.1, add_weighted=False):
    """Returns image1 * mask  + image2 * mask_inverse"""
    mask = mask / 255
    mask = mask.astype(np.uint8)

    mask_inv = np.invert(mask) / 255.0
    mask_inv = mask_inv.astype(np.uint8)
    fg = fg_image * mask
    if add_weighted:
        res = cv2.addWeighted(fg, alpha, bg_image, 1 - alpha, 0, bg_image)
    else:
        bg = bg_image * mask_inv
        res = fg + bg
    return res


def mask_image(fg_image, mask):
    """To generate basic mask image for the given image.
    Returns the image with the bg removed."""
    mask = mask / 255
    mask = mask.astype(np.uint8)
    # mask_inv = np.invert(mask) / 255.0
    # mask_inv = mask_inv.astype(np.uint8)
    fg = fg_image * mask
    return fg


def fuse(fixed, moving, resize=True):
    """Gets two images as input and returns the fused image"""
    if len(fixed.shape) == 3:
        fixed = cv2.cvtColor(fixed, cv2.COLOR_BGR2GRAY)
    if len(moving.shape) == 3:
        moving = cv2.cvtColor(moving, cv2.COLOR_BGR2GRAY)
    if fixed.shape != moving.shape:
        print("fusing shapes are not matching")
        if resize:
            print("resizign second image for fusing")
            moving = cv2.resize(moving, dsize=fixed.shape[::-1])
    fuz = np.zeros([fixed.shape[0], fixed.shape[1], 3], dtype=fixed.dtype)
    fuz[:, :, 1] = fixed
    fuz[:, :, 2] = moving
    return fuz


def show_fuse(fixed, moved, win="img", time=30, destroy=False, k=-1):
    """To show the fused image, taking input of fixed and moving images
    Displays the fused image."""
    fuz = fuse(fixed, moved)
    k = show(fuz, win, time, destroy, k)
    return k


def blend(fixed, moved, x_start=None):
    """Gets two images as input and returns the blended image"""
    if x_start is None:
        fixed_gray = cv2.cvtColor(fixed, cv2.COLOR_BGR2GRAY)
        ret, fixed_th = cv2.threshold(fixed_gray, 1, 255, cv2.THRESH_BINARY)
        bbox = cv2.boundingRect(fixed_th)
        fixed[:, bbox[0] :, :] = moved[:, bbox[0] :, :]
    else:
        fixed[:, x_start:, :] = moved[:, x_start:, :]
    return fixed


def show_blend(fixed, moved, win="img", time=30, destroy=False, k=-1):
    """To show the blended image, taking input of fixed and moving images
    Displays the blended image"""
    blended = blend(fixed, moved)
    k = show(blended, win, time, destroy, k)
    return k


def concat(fixed, moved, axis=1):
    """Gets two images as input and returns the concatenated image"""
    concated = np.concatenate((fixed, moved), axis=axis)
    return concated


def show_concat(fixed, moved, win="img", time=30, destroy=False, k=-1):
    """To show the Concatenated image, taking input of fixed and moving images
    Displays the concatenated image"""
    concated = concat(fixed, moved)
    k = show(concated, win, time, destroy, k)
    return k


def flicker(im1, im2, win="flick", time=500, destroy=False, count=2):
    """To show the flickering window image by taking input as two images"""
    cv2.namedWindow(win, cv2.WINDOW_GUI_NORMAL)
    flag = 0
    for i in range(count):
        if flag == 0:
            cv2.imshow(win, im1)
        else:
            cv2.imshow(win, im2)
        flag = not flag
        k = cv2.waitKey(time)
        if k == 27:
            break
    if destroy:
        cv2.destroyWindow(win)


def mat_plot(y, t=None, xlabel=None, ylabel=None, color=None, title="plot", block=True):
    """To show a matplot window"""
    plt.title(title)
    if t is None:
        t = np.arange(len(y))
    # plt.autoscale(enable=False, axis='y', tight=None)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(t, y, color=color)
    plt.show(block=block)


class ThreadShow:
    """show with threading"""

    def __init__(self, queue_size=20, time_=1):
        self.watch_q = Queue(maxsize=1)
        self.thread = Thread(target=self.update)
        self.thread.daemon = True
        self.q = Queue(maxsize=queue_size)
        self.time = time_

    def start(self):
        """start threading"""
        self.thread.start()

    def put(self, img):
        """put image to queue"""
        print("putting image into queue")
        self.q.put(img)
        print("put Done")

    def stop(self):
        """stop threading"""
        self.watch_q.put("EOF")

    def update(self):
        """Show queue items in a while loop"""
        counter = 0
        while True:
            print("********** updating *************")
            if self.watch_q.qsize():
                print("Thread  stopping ")
                break
            if not self.q.empty():
                img = self.q.get()
                print("image shape", img.shape)
                show(img, "Result", time=self.time)
            else:
                T.sleep(0.1)  # Rest for 10ms, we have a full queue
        cv2.destroyAllWindows()


class ShowProcess(BaseProcess):
    """Class for showing images in que"""

    def do_func(self, data):
        """data: img, win_name, time
        call show with this data.
        """
        # print('img:',img.shape)
        if len(data) == 2:
            img, win_name = data
            time = 200
        if len(data) == 3:
            img, win_name, time = data
        show(img, win_name, time=time)

    def on_stop(self):
        """Function to be executed on stop"""
        print("destroying all windows")
        cv2.destroyAllWindows()


def pylab_show():
    """pylab based imshow"""

    z = random.random((50, 50))  # Test data

    imshow(z, cmap=get_cmap("Spectral"), interpolation="nearest")
    # show()


def show_contours(contours: List[CntrL], img=None, H=None, W=None, color=(255, 0, 0), thickness=3, win="cntrs", time=0, k=-1):
    """Draw contours on image given
    or create empty image of HxW
    or create empty image with min max dimension
    """
    contours = np.array(contours)
    # assert len(contours.shape)==3, 'Expecting [[[x,y],],]'
    if img is None:
        if H is None or W is None:
            H = 0
            W = 0
            for cntr in contours:
                if len(cntr):
                    hw = np.max(cntr, 0)
                    h = hw[1]
                    w = hw[0]
                    if h > H:
                        H = h
                    if w > W:
                        W = w
        img = np.zeros((H, W), dtype=np.uint8)
    # contours = np.array(contours).reshape((len(contours),-1, 1, 2)).astype(np.int32)
    # cv2.drawContours(img, contours, -1, color, thickness)
    draw_cntrs(contours, img, color=color, thickness=thickness)
    k = show(img, win=win, time=time, k=k)

    return k


class TestShowUtils(unittest.TestCase):
    """Unit test function created to check the show module is working or not"""

    def uitest_show(self):
        """test show and fuse"""
        leftpath = os.path.join("samples/rssi_crack.jpg")
        imL = cv2.imread(leftpath)
        k = show(imL, win="img0", time=0, destroy=False, k=-1)

    def uitest_fuse(self):
        """test show and fuse"""
        leftpath = os.path.join("samples/rssi_crack.jpg")
        rightpath = os.path.join("samples/fisheye_crop_sample.jpg")
        imL = cv2.imread(leftpath)
        imR = cv2.imread(rightpath)
        k = show_fuse(imL, imR, win="imgfuse", time=0, destroy=False, k=-1)

    def test_masked_add(self):
        """Test masked_add"""
        fixed_path = os.path.join("samples/image1.png")
        moved_path = os.path.join("samples/image2.png")

        fg_image = cv2.imread(fixed_path)
        bg_image = cv2.imread(moved_path)

        mask = np.zeros((bg_image.shape[0], bg_image.shape[1], 3), dtype=np.uint8)

        res = masked_add(fg_image, bg_image, mask, alpha=0.1, add_weighted=False)
        self.assertNotIsInstance(res, type(None))
        cv2.imwrite("show_masked_add.jpg", res)

    def test_fuse(self):
        """Test fuse"""
        fixed_path = os.path.join("samples/image1.png")
        moved_path = os.path.join("samples/image2.png")

        fixed = cv2.imread(fixed_path)
        moving = cv2.imread(moved_path)

        fuz = fuse(fixed, moving)
        self.assertIsNotNone(fuz)
        cv2.imwrite("show_fuz.jpg", fuz)

    def test_blend(self):
        """Test Blend"""
        fixed_path = os.path.join("samples/image1.png")
        moved_path = os.path.join("samples/image2.png")

        fixed = cv2.imread(fixed_path)
        moved = cv2.imread(moved_path)

        blend = fuse(fixed, moved)
        self.assertIsNotNone(blend)
        cv2.imwrite("show_blend.jpg", blend)

    def uitest_show_contours(self):
        """Test show_contours"""
        cntrs = [[[379, 364], [633, 316], [854, 321], [988, 580]], [[686, 763], [729, 441], [1363, 427], [1353, 705]]]
        cntrs = np.array(cntrs).astype(np.int64)
        k = show_contours(cntrs)

    def uitest_thread_show(self):
        """Test thread show"""

        thread_obj = ThreadShow(queue_size=20, time_=100)
        thread_obj.start()
        folderpath = "samples/transform_test"
        files = get_all_files(folderpath, include_type="image")
        print("files", files)
        for img_path in files:
            img = cv2.imread(img_path)
            thread_obj.put(img)
            T.sleep(1)
        thread_obj.stop()
        T.sleep(1)

    def uitest_show_process(self):
        """ "test show process"""
        show_proc = ShowProcess()
        show_proc.start()
        for i in range(3):
            img = np.random.rand(100, 100, 3) * 255
            img = img.astype(np.uint8)
            show_proc.send(img)  # will put into que and will be displayed
        show_proc.stop()
        show_proc.join()


if __name__ == "__main__":
    test_obj = TestShowUtils()
    test_obj.uitest_show()
    test_obj.uitest_fuse()
    # TO-DO
    # test_obj.uitest_show_contours()
    # test_obj.uitest_thread_show()
    # test_obj.uitest_show_process()

    # test_obj.test_masked_add()
    # test_obj.test_fuse()
    # test_obj.test_blend()

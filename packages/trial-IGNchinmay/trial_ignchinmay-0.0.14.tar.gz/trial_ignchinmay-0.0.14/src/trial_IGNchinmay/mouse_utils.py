# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : MousePts.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To handlle mouse events from the screen."""
from typing import List
import unittest
import cv2
import numpy as np
from trial_IGNchinmay.draw_utils import put_texts
from trial_IGNchinmay.typehint_utils import CntrL, Optional


class MousePts:
    """To select the mouse points on image."""

    def __init__(self, img=None, windowname="image", sz=None, thick=None, rect_thick=None, show_text=True, contour_count=None, win_x=None, win_y=None, win_width=None, win_height=None, destroy_flag=False):
        self.windowname = windowname
        if img is not None:
            self.img1 = img.copy()
            self.img = self.img1.copy()

        # list of list of points, eg: [[(x1,y1),x2,y2)], [(x3,y3),(x4,y4)}]]
        self.contrs: Optional[List[CntrL]] = []
        self.pts = []
        self.curr_pt = None  # mouse position
        self.old_pt = None  # previous mouse position
        self.mousedn_pt = None  # where mouse was clicked
        self.contr_indx = None
        self.selected_pt_index = None
        self.addpts = False
        self.sz = sz  # track rectangle size
        self.select_flag = False  # indicates if a trackbox is selected
        self.thick = thick
        self.rect_thick = rect_thick
        self.win_x = win_x
        self.win_y = win_y
        self.win_width = win_width
        self.win_height = win_height
        self.color = (255, 0, 0)
        self.selected_color = (0, 255, 0)
        self.selected_crect_olor = (0, 0, 255)
        self.escape_count = 1
        self.mid_pint_find = False
        self.mid_points_list = []
        self.mode = None
        self.auto_adjust = False
        self.roi_type = None
        self.show_text = show_text
        self.contour_count = contour_count  # Max number of contours that can be created
        self.destroy_flag = destroy_flag
        self.h = None  # image height
        self.w = None  # image width

    def mouse_callback(self, event, x, y, flags, param): # pylint: disable=unused-argument
        """Handle calback on mouse events.
        Args:
            event (NumpyArray): The mouse click event is tracked.
            x (int): x Coordinate of the point to select.
            y (int): x Coordinate of the point to select.
        """
        x, y = self.sanity(x, y)
        self.curr_pt = [x, y]
        if event == cv2.EVENT_LBUTTONUP:
            # Check if clcik is near any point
            if self.select_flag:
                self.select_flag = False
                return

            if self.mid_pint_find:
                self.mid_points_list.append(self.curr_pt)
                if len(self.mid_points_list) == 2:
                    mid_x = int((self.mid_points_list[0][0] + self.mid_points_list[1][0]) // 2)
                    mid_y = int((self.mid_points_list[0][1] + self.mid_points_list[1][1]) // 2)
                    self.mid_pint_find = False
                    self.mid_points_list = []
                    self.curr_pt = [mid_x, mid_y]
                    if self.selected_pt_index is not None:
                        self.contrs[self.contr_indx][self.selected_pt_index] = [mid_x, mid_y]
                        return
                    if self.contrs:
                        self.contrs.append([[mid_x, mid_y]])
                        self.contr_indx = 0
                        self.addpts = True
                        return
                else:
                    return
            else:
                for j, cntr in enumerate(self.contrs):
                    for i, pt in enumerate(cntr):
                        if abs(x - pt[0]) < self.sz and abs(y - pt[1]) < self.sz:
                            self.select_flag = True
                            self.selected_pt_index = i
                            self.contr_indx = j
                            self.mousedn_pt = [x, y]
                            break

            if not self.select_flag and self.addpts and self.contr_indx is not None:
                if self.contr_indx >= len(self.contrs):
                    self.contrs.append([])
                selected_item = self.contrs[self.contr_indx]
                if not isinstance(selected_item, list):
                    selected_item = selected_item.tolist()

                selected_item.append(self.curr_pt)
                self.contrs[self.contr_indx] = selected_item
                self.selected_pt_index = len(self.contrs[self.contr_indx]) - 1

        if event == cv2.EVENT_MOUSEMOVE:
            if self.select_flag:  # continously update selected point in pts
                # if (self.auto_adjust and (self.selected_pt_index == 0 or self.selected_pt_index == 2)):
                if self.auto_adjust and self.selected_pt_index == 2:
                    self.contrs[self.contr_indx][self.selected_pt_index] = [x, self.contrs[0][self.selected_pt_index][1]]
                elif self.roi_type == "rect":
                    self.contrs[self.contr_indx] = self.make_rect(self.contrs[self.contr_indx], self.selected_pt_index, self.curr_pt)
                else:
                    self.contrs[self.contr_indx][self.selected_pt_index] = self.curr_pt

    def select_contr(self, img, contrs: List[CntrL], numpts=5, closed=True, contr_indx=None, addcontr=True, addpts=True, color=(255, 0, 0), line_color=(255, 255, 255), roi_type=None, edit_mode=False, callback=None, txts_list=None, **params): # pylint: disable=too-many-statements,too-many-branches
        """Select points in image and returns roi. Input: list of pts.
        Args:
            img (NumpyArray): Full Image pixels.
            contrs (list, optional): list of countrs seleted, defaultsto []
            numpts (int, optional): Number of points selected, defaultsto 5
            closed (bool, optional): To confirm wether the contr is
                                        closed or not, defaults to True
            contr_indx (int, optional): Index of each contr, defaults to None
            addcontr (bool, optional): To check wether to add new contr or not, defaults to True
            addpts (bool, optional): If addcontr is true need wether we color (tuple, optional):
                                     Color of the points selected,defaults to (255, 0, 0)
            roi_type (str, optional):roi type- '4pt', 'rect', None
            postprocess_func: function to be applied on points after change
        Returns:
            NumpyArray: roi contrs.
        """
        assert img is not None
        assert not (addcontr is True and contr_indx is not None), "Either addcontr or contr_indx only should be not None"
        if contr_indx:
            assert contr_indx <= len(contrs)
        self.color = color

        if self.pts is None:
            self.pts = []

        # Contour and contour index setting
        self.contrs = contrs
        if addcontr and contr_indx is None:
            contr_indx = len(contrs)
            self.contr_indx = contr_indx
        elif addcontr is False and contr_indx is None:
            if contrs:
                contr_indx = len(contrs) - 1
            else:
                contr_indx = 0
            self.contr_indx = contr_indx

        if addpts is True:
            print("adjust the roi in image or create new roi")
            self.addpts = addpts
        else:
            print("addpts == false or len(self.pts)<numpts , can only edit pts")

        self.h, self.w = img.shape[:2]
        mindim = min(self.h, self.w)
        if self.sz is None:
            self.sz = mindim // 50
        if self.thick is None:
            self.thick = max(2, mindim // 600)
        self.roi_type = roi_type

        cv2.namedWindow(self.windowname, cv2.WINDOW_GUI_NORMAL)
        if self.win_width and self.win_height:
            cv2.resizeWindow(self.windowname, self.win_width, self.win_height)
        if self.win_x and self.win_y:
            cv2.moveWindow(self.windowname, self.win_x, self.win_y)
        cv2.setMouseCallback(self.windowname, self.mouse_callback)

        k = -1
        ctr_copy = self.contrs.copy()
        # x_txt = ctr_copy[0][2][0] + 200
        while True:
            img_copy = img.copy()

            if txts_list is None:
                if self.auto_adjust:
                    txts_list = ["Move four trackbars of ROI to the corners of 4 plates,", "Make sure to include 5 ties within ROI,", "Press Esc to save & Close the ROI adjust window"]

                elif edit_mode and not self.auto_adjust:
                    txts_list = ["Move four trackbars of ROI to the corners of 4 plates,", "Make sure to include 5 ties within ROI,", "Press Esc to save & Close the ROI calib Window"]
                else:
                    txts_list = ["n -new shape", "m -mid point", "d -line deletion"]
                    if not closed:
                        txts_list.extend(["p -point deletion", "z -undo", "a -append", "Esc - close window"])
                    else:
                        txts_list.extend([f"Draw roi by clicking {numpts} points clockwise-", "starting with top-left.", "Press Enter/Esc to quit."])
            # find dynamic value for given video resolution
            v_space = img_copy.shape[1] // 40
            thickness = max(2, img_copy.shape[1] // 700)

            if self.show_text:
                self.img1 = put_texts(img_copy, test_tuple_list=txts_list, txt_thickness=thickness, v_space=v_space, draw_bg=False)

            if self.contrs and self.contr_indx is not None and self.contr_indx < len(self.contrs):
                self.pts = self.contrs[self.contr_indx]
            else:
                self.pts = []

            if callback is not None:
                if not (self.old_pt and self.curr_pt and self.old_pt == self.curr_pt):
                    self.old_pt = self.curr_pt
                    callback(self.contrs, self.contr_indx, **params)

            pts = np.array(self.pts, np.int32)
            is_closed = True if len(pts) == numpts and closed else False # pylint: disable=simplifiable-if-expression
            if len(pts) > 0 and len(pts) <= numpts:
                cv2.polylines(img_copy, [pts], is_closed, line_color, thickness=self.thick)

            for p in self.mid_points_list:
                cv2.circle(img_copy, tuple(p), self.sz, (0, 0, 255), thickness=-1)

            for indx, cntr in enumerate(self.contrs):
                corner_pts = np.array(cntr, np.int32)
                for n, pt in enumerate(corner_pts):
                    # pt[1],pt[0] = self.sanity(pt[1],pt[0])
                    start = (int(pt[0] - self.sz), int(pt[1] - self.sz))
                    end = (int(pt[0] + self.sz), int(pt[1] + self.sz))
                    rect_color = self.color
                    if self.contr_indx == indx:
                        rect_color = self.selected_color
                        if self.selected_pt_index == n:
                            rect_color = self.selected_crect_olor
                    if self.rect_thick is None:
                        self.rect_thick = self.thick + 2
                    cv2.rectangle(img_copy, start, end, rect_color, thickness=self.rect_thick)

            if len(pts) >= numpts:
                self.escape_count = 1
                self.addpts = False

            for i, cnt in enumerate(self.contrs):
                if i != self.contr_indx:
                    cv2.polylines(
                        img_copy,
                        [np.array(cnt, np.int32)],
                        closed,
                        (255, 255, 255),
                        self.thick,
                    )

            cv2.imshow(self.windowname, img_copy)
            if k != ord("n"):
                k = cv2.waitKeyEx(30)
            if k in (27,13):
                self.addpts = False
                self.select_flag = False
                self.escape_count += 1
                if self.escape_count >= 2:
                    if self.contr_indx is not None and len(self.contrs) > self.contr_indx:
                        if len(self.contrs[self.contr_indx]) == 0:
                            self.contrs.pop(self.contr_indx)
                    break

            # if edit_mode:
            #     if k != -1:
            #         # print("Only moving 4 track bars supported!")
            #     continue

            if k == ord("a"):  # 'a - append point'
                if not closed:
                    self.escape_count = 0
                    self.addpts = True
                    self.select_flag = False
                    self.mid_points_list = []
            if k == ord("n"):  # 'n - new line '
                self.escape_count = 0
                self.contr_indx = len(self.contrs)
                if self.contour_count is not None:  # Limiting the number of new added contours to contour count
                    self.contr_indx = min(self.contour_count, self.contr_indx)
                self.select_flag = False
                self.addpts = True
                k = -1
            if k == ord("z"):  # 'z - undo '
                if not closed:
                    if len(self.contrs) > self.contr_indx:
                        selected_line = self.contrs[self.contr_indx]
                        if not isinstance(selected_line, list):
                            selected_line = selected_line.tolist()
                        if selected_line:
                            selected_line.pop(self.selected_pt_index)
                            self.selected_pt_index = len(selected_line) - 1
                            self.contrs[self.contr_indx] = selected_line
            if k == ord("m"):  # 'm - mid point calculation '
                if closed:
                    self.mid_pint_find = True
                    self.escape_count = 0
            if k == ord("d"):  # 'd - line deletion, aloows only when edit mode False'
                if self.contr_indx is not None:
                    if len(self.contrs) > self.contr_indx:
                        self.contrs.pop(self.contr_indx)
                        if self.contrs:
                            self.contr_indx -= 1
                        else:
                            self.contr_indx = None
                        self.select_flag = False
            if k == ord("p"):  # 'p - point deletion '
                if self.contr_indx is not None and self.selected_pt_index is not None and not closed:
                    if len(self.contrs) > self.contr_indx:
                        selected_line = self.contrs[self.contr_indx]
                        if not isinstance(selected_line, list):
                            selected_line = selected_line.tolist()
                        if selected_line:
                            selected_line.pop(self.selected_pt_index)
                            self.contrs[self.contr_indx] = selected_line
                        if self.contrs:
                            self.contr_indx -= 1
                        else:
                            self.contr_indx = None
                        self.select_flag = False

        cv2.setMouseCallback(self.windowname, lambda *args: None)
        if not self.destroy_flag:
            cv2.destroyWindow(self.windowname)

        return self.contrs

    def select_rect(self, img, roi: CntrL = None, edit_mode=False, auto_adjust=False, callback=None, line_color=(255, 255, 255), txts_list=None, **params):
        """Wrapper on select_roi, to select a rectangle"""
        return self.select_roi(img, roi=roi, edit_mode=edit_mode, auto_adjust=auto_adjust, rect_mode=True, callback=callback, line_color=line_color, txts_list=txts_list, **params)

    def select_roi(self, img, roi: CntrL = None, edit_mode=False, auto_adjust=False, rect_mode=False, callback=None, line_color=(255, 255, 255), txts_list=None, **params):
        """To select four point roi
        Args:
            img (Numpy array): Full Image pixels.
            roi (NumpyArray , optional): Selected ROI region, defaults to None
            edit_mode(Bool): User can only edit, can not delete, can not add more points
        Returns:
            NumpyArray: Selected ROI contrs
        """
        self.h, self.w = img.shape[:2]
        mindim = min(self.h, self.w)
        if roi is None:
            if self.sz is None:
                self.sz = mindim // 20
            if self.thick is None:
                self.thick = max(2, mindim // 200)
            contrs = [[[self.w // 4, self.h // 4], [self.w * 3.2 // 4, self.h // 3.4], [self.w * 3.5 // 4, self.h * 3.1 // 4], [self.w // 3.6, self.h * 3.3 // 4]]]
        else:
            contrs = [roi]
        roi = []
        self.auto_adjust = auto_adjust
        if rect_mode:
            roi_type = "rect"
        else:
            roi_type = "4pt"
        rois = self.select_contr(img, contrs=contrs, numpts=4, closed=True, contr_indx=None, addcontr=False, addpts=True, color=(255, 255, 255), roi_type=roi_type, edit_mode=edit_mode, callback=callback, txts_list=txts_list, line_color=line_color, **params)
        if rois:
            roi = rois[-1]
        return roi

    def sanity(self, x, y):
        """Force point inside of image boundaries"""
        assert self.w is not None and self.h is not None
        x = max(0, x)
        x = min(x, self.w)
        y = max(0, y)
        y = min(y, self.h)
        return x, y

    def make_rect(self, contr, index, curr_pt):
        """make a rectangle using contr points and current point"""
        diag_indx = (index + 2) % 4
        p1 = contr[diag_indx]
        p2 = curr_pt
        x1, y1 = min(p1[0], p2[0]), min(p1[1], p2[1])
        x2, y2 = max(p1[0], p2[0]), max(p1[1], p2[1])
        contr = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
        return contr


class MouseListen:
    """Get mouse position of left click"""

    def __init__(self) -> None:
        """initialising mouse pos check"""
        self.pos = None
        self.listener = None

    def on_click(self, x, y, button, pressed):
        """on click"""
        if pressed:
            print("Mouse clicked:", x, y, button)
            self.pos = [x, y]
            self.listener.stop()

    def on_move(self, x, y):
        """on move"""
        # print("Mouse moved to ({0}, {1})".format(x, y))

    def on_scroll(self, x, y, dx, dy):
        """on scroll"""
        # print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

    def wait_for_mouse(self):
        """wait for mouse click"""
        from pynput import mouse  # pylint: disable=import-outside-toplevel

        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()
        print("waiting for mouse click...")
        self.listener.join()
        print("return pos:", self.pos)
        return self.pos


class TestMouseUtils(unittest.TestCase):
    """Test methods"""

    def callback(self, contrs, contr_indx, **params):
        """callback on select mouse point selection this way
        we can use mouse points in projects!
        Make your own callback as neded.extra params needed
        can be passed in **params see usage example below"""
        # print("callback called!", "contrs:", contrs, "contr_indx:", contr_indx, "params:", params)

    def uitest_mouse_pts(self):
        """test MousePts"""
        imagep = "samples/rssi_crack.jpg"
        img = cv2.imread(imagep)
        mouse_obj = MousePts(img)
        # Demo contour, roi,rect selection
        pts = mouse_obj.select_contr(img, contrs=[], numpts=6, closed=True, contr_indx=None)
        print("pts", pts)
        roi = mouse_obj.select_roi(img)
        print("ROI", roi)
        roi = mouse_obj.select_rect(img)
        print("ROI", roi)
        params_ = {"a": 1}
        roi = mouse_obj.select_rect(img, callback=lambda contrs, contr_indx, **params: print("callback!"), **params_)
        print("ROI", roi)

    def uitest_mouse_listen(self):
        """test MouseListen"""
        mouse_check = MouseListen()
        pos = mouse_check.wait_for_mouse()
        print("pos:", pos)


if __name__ == "__main__":
    test_obj = TestMouseUtils()
    test_obj.uitest_mouse_pts()
    test_obj.uitest_mouse_listen()

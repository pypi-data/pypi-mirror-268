# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : trapezoid_crop_utils.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To generate crop image and json based on input contour

RUN: p3 -m trial_IGNchinmay.transform_utils
"""

from os import makedirs
from typing import Optional
import unittest
import cv2
import numpy as np

import trial_IGNchinmay as icv
from trial_IGNchinmay.draw_utils import draw_cntrs
from trial_IGNchinmay.contour_utils import direction_boxsort, get_contour_area, getfitbox, getbbox, cv2lab, get_contour_intersection, is_lab_cntr
from trial_IGNchinmay.json_utils import compare_json, read_json
from trial_IGNchinmay.img_utils import compare_imgs
from trial_IGNchinmay.labelme_utils import create_labelme_json, write_label_json, cleanup_json
from trial_IGNchinmay.mouse_utils import MousePts
from trial_IGNchinmay.geom_utils import euclidean


def get_box(
    crop_cntr,
    crop_type="fitbox",
    vertical_first: Optional[bool] = True,
):
    """Create box for given contour based on box type
    Returns the box around the contour"""

    assert len(crop_cntr) >= 3, "need atleast three points in crop_cntr"
    crop_cntr = np.array(crop_cntr, dtype=np.float32)

    if crop_type == "trapezoid":
        assert len(crop_cntr) == 4, "trapezoid crop need 4 point roi"
    elif crop_type == "fitbox":
        crop_cntr = getfitbox(crop_cntr, verticalfirst=None)
    elif crop_type == "bbox":
        crop_cntr = getbbox(crop_cntr, verticalfirst=None)
    else:
        raise ValueError(f"crop type {crop_type} not supported")
    box = np.array(crop_cntr, dtype=np.float32)

    # Sorting points for aligning vertically or horizontally
    if vertical_first is not None:
        box = direction_boxsort(box, unit_vec=(0, 1), vertical_sort_first=vertical_first)
    return box

def expand_box(roi, w1=None, h1=None, pad_l=0, pad_r=0, pad_t=0, pad_b=0, expand_dest=True):
    """Function used to expand the selected ROI of Image.
    Args:
        roi : ROI to be expand
        w1,h1 : width and height of destination rectangle
        pad_l (int, optional): Along left, defaults to 0
        pad_r (int, optional): Along right, defaults to 0
        pad_t (int, optional): Along top, defaults to 0
        pad_b (int, optional): Along bottom, defaults to 0
    Returns: src_box expanded, dst_box expanded, forward transform matrix
    """
    roi = np.array(roi, dtype=np.float32)
    pt1, pt2, pt3, _ = roi
    if w1 is None:
        w1 = euclidean(pt1, pt2)
    if h1 is None:
        h1 = euclidean(pt2, pt3)

    dst_points = np.array([[0, 0], [w1, 0], [w1, h1], [0, h1]], dtype=np.float32)

    tr = cv2.getPerspectiveTransform(roi, dst_points)
    tr_inv = np.linalg.inv(tr)  # to map from dst to src
    x1, y1 = 0, 0
    dst_expanded = np.array(
        [
            [x1 - pad_l, y1 - pad_t],
            [x1 + w1 + pad_r, y1 - pad_t],
            [x1 + w1 + pad_r, y1 + h1 + pad_b],
            [x1 - pad_l, y1 + h1 + pad_b],
        ],
        dtype=np.float32,
    )
    src_expanded = transform_contour(np.squeeze(dst_expanded), tr_inv)
    # src_expanded = np.squeeze(src_expanded)
    if expand_dest:
        w1 += pad_l + pad_r
        h1 += pad_t + pad_b
    dst_points = np.array([[0, 0], [w1, 0], [w1, h1], [0, h1]], dtype=np.float32)
    tr = cv2.getPerspectiveTransform(src_expanded, dst_points)
    dst_w_h = (w1, h1)  # exapnded dst width and height
    return src_expanded, dst_w_h, tr

def get_box_dims(box):
    """get h and w of box"""
    pt1, pt2, pt3, _ = box
    width = euclidean(pt1, pt2)
    height = euclidean(pt2, pt3)
    return int(height), int(width)

def transform_crop(
    image,
    crop_cntr,
    mask=None,
    json_dict=None,
    crop_type="trapezoid",
    h1=None,
    w1=None,
    pad_l=0,
    pad_r=0,
    pad_t=0,
    pad_b=0,
    tr=None,
    interpolation=cv2.INTER_CUBIC,
    expand_dest=True,
    vertical_first: Optional[bool] = True,
    label_list=(),  # list of labels to be retained in crop json, if empty then all labels will be retained
):
    """Function that asks user to click on four corner points of trapezoidal shape and
    generates rectangular transformed image of selected trapezoid. ht and wd are height and
    width of final crop image, by default it will be calculated based on input points.
    Args:
        crop_cntr: Points to crop
        image : Input image
        mask : Mask, defaults to None
        json_dict : labelme json data
        crop_type : 'trapezoid','fitbox','bbox'
        h1 : final crop image height, defaults to None
        w1 : final crop image width, defaults to None
        pad_l: expansion towrds left, defaults to 0
        pad_r : expansion towrds right, defaults to 0
        pad_t : expansion towrds top, defaults to 0
        pad_b : expansion towrds bottom, defaults to 0
        expand_dest : if True, dest crop dim will be expanded with input pad values.
        vertical_first: points will will sorted along unit vector first then orthogonal
        tr : Transform Matrix
        interpolation : Type of interpolation eg: cv2.INTER_CUBIC, defaults to cv2.INTER_LINEAR
    Returns:
        crop_image, crop_mask, json_dict, transform_matrix
    """
    box = get_box(crop_cntr, crop_type=crop_type, vertical_first=vertical_first)

    src_expanded, dst_w_h, _ = expand_box(box, pad_l=pad_l, pad_r=pad_r, pad_t=pad_t, pad_b=pad_b, expand_dest=expand_dest)

    if w1 is None:
        w1 = dst_w_h[0]
    elif expand_dest:
        w1 += pad_l + pad_r
    if h1 is None:
        h1 = dst_w_h[1]
    elif expand_dest:
        h1 += pad_t + pad_b


    # Calculate transform matrix if not provided
    if tr is None:
        dst_points = np.array([[0, 0], [w1, 0], [w1, h1], [0, h1]], dtype=np.float32)
        tr = cv2.getPerspectiveTransform(src_expanded, dst_points)


    # Apply transform
    crop_image = cv2.warpPerspective(image, tr, (int(w1), int(h1)), flags=interpolation)
    if json_dict is not None:
        json_dict = trapezoid_crop_json(json_dict, tr, int(h1), int(w1), label_list=label_list)
    if mask is not None:
        crop_mask = cv2.warpPerspective(mask, tr, (int(w1), int(h1)), flags=interpolation)
    else:
        crop_mask = None
    return crop_image, crop_mask, json_dict, tr


def transform_paste(full_json_dict, crop_json_dict, label_list=()):
    """To map crop json to full json using transform matrix from crop_json.
    Map only those shapes which are in label_list if label_list is not empty.
    Returns the full json with the crop mapped points ##
    """
    crop_json_dict_copy = crop_json_dict.copy()
    tr_matrix = crop_json_dict_copy["tr_matrix"]
    for i, shape in enumerate(crop_json_dict_copy["shapes"]):
        if label_list and shape["label"] not in label_list:
            continue
        cntr_pts = shape["points"]
        tr_inv = np.linalg.inv(tr_matrix)
        trnsform_cntr = transform_contour(cntr_pts, tr_inv)
        shape["points"] = np.squeeze(trnsform_cntr).tolist()
        full_json_dict["shapes"].append(shape)
    return full_json_dict


def transform_img(img, target_ht, target_wd, tr, flag=cv2.INTER_CUBIC):
    """Function to apply perspective transform.
    Args:
        img: Input image
        target_ht: Fixed image height
        target_wd: Fixed image width
        tr : Transformation matrix
    Returns:
        image after transormation
    """
    if tr.shape == (2, 3):
        moved = cv2.warpAffine(img, np.array(tr), (target_wd, target_ht), flags=flag)
    else:
        moved = cv2.warpPerspective(img, np.array(tr), (target_wd, target_ht), flags=flag)
    return moved


def transform_contour(point_list, tr):
    """Function to apply transform matrix on point list
    Args:
        point_list : list of points
        tr : Transformation matrix
    Returns:
        points after transformation
    """
    tr = np.array(tr, dtype=np.float64)
    contours = np.array([point_list], dtype=np.float32)
    if tr.shape == (2, 3):
        out_point_list = cv2.transform(contours, tr)
    else:
        out_point_list = cv2.perspectiveTransform(contours, tr)  # .astype(int)
    out_point_list = np.squeeze(out_point_list).astype(np.float32)
    return out_point_list


def select_roi_expanded(frame, x_expn_fact=0, y_expn_fact=0):
    """To select the ROI point based on mouse click events
    Returns: list, NumpyArray: selected ROI points.
    """
    mouse_obj = MousePts(frame)
    roi = mouse_obj.select_roi(frame)
    print("roi:", roi)
    assert len(roi) == 4, "No ROI selected"
    roi = resize_box(roi, x_expn_fact=x_expn_fact, y_expn_fact=y_expn_fact)
    return roi


def resize_box(box, x_expn_fact=0.1, y_expn_fact=0):
    """To expand the selected ROI points
    Returns:expanded box
    """
    tl, _, br, bl = box
    width = euclidean(bl, br)
    pad_l, pad_r = int(width * x_expn_fact), int(width * x_expn_fact)
    height = euclidean(tl, bl)
    pad_t, pad_b = int(height * y_expn_fact), int(height * y_expn_fact)
    box_expanded, _, _ = expand_box(box, pad_l=pad_l, pad_r=pad_r, pad_t=pad_t, pad_b=pad_b)
    return box_expanded


def autocrop(org, box, mask=None):
    """Generate cropped image and expanded box points.
    Args:
        org : The original Image
        box : the coordinates of the contour (usually the length of the list should be 4 ; the extremal points)
    Returns:
        Cropped image, expanded box and Mask of cropped image
    """
    mask_cropped = None
    img = org.copy()
    im_gray = cv2.cvtColor(org, cv2.COLOR_RGB2GRAY)
    (thresh, im_bw) = cv2.threshold(im_gray, 1, 255, cv2.THRESH_BINARY | cv2.THRESH_BINARY)
    col_sum = np.sum(im_bw, axis=0)
    col_sum_max = max(col_sum)
    rows, cols = im_bw.shape
    hz = []
    for x in range(0, cols):
        if col_sum[x] == col_sum_max:
            hz.append(x)
            break
    for x in reversed(range(0, cols)):
        if col_sum[x] == col_sum_max:
            hz.append(x)
            break
    left_dist = hz[0]
    right_dist = org.shape[1] - hz[1]
    cropped = img[0:rows, hz[0] : hz[1]]
    if mask is not None:
        mask_cropped = mask[0:rows, hz[0] : hz[1]]
    box, _, _ = expand_box(box, pad_l=-left_dist, pad_r=-right_dist, pad_t=0, pad_b=0)
    return cropped, box, mask_cropped


def trapezoid_crop_json(json_dict, tr, target_h, target_w, label_list=()):
    """Transform each contours in json dict based on tranformation matrix.
    Returns the transformed json"""
    shape_list = json_dict["shapes"]
    # roi = [[0, 0], [target_W, 0], [target_W, target_H], [0, target_H]]
    roi = [[0, 0], [target_w, 0], [target_w, target_h], [0, target_h]]
    crop_json = create_labelme_json()
    crop_json["imagePath"] = json_dict.get("imagePath", [])
    crop_json["checksum"] = json_dict.get("checksum", [])
    crop_json["tr_matrix"] = tr.tolist()
    # print("No of trapi crops:", len(shape_list))
    for shape in shape_list:
        # print('trapi crop shape:', shape['label'])
        # keep only the label in the list if not empty, else keep all
        if label_list and shape["label"] not in label_list:
            continue
        contour = shape["points"]
        t_contour = transform_contour(contour, tr)
        t_contour = cv2lab(t_contour)
        intersection_cntrs = get_contour_intersection(t_contour, roi)
        if any(intersection_cntrs):
            # print('intersection_cntr:', len(intersection_cntrs))
            for intersection_cntr in intersection_cntrs:
                shape_copy = shape.copy()
                if not is_lab_cntr(intersection_cntr):
                    intersection_cntr = cv2lab(intersection_cntr)
                shape_copy["points"] = intersection_cntr
                crop_json["shapes"].append(shape_copy)
    # print('trapezoid_crop_json time taken:', time.time() - start)
    # print('trapi crop json2:', len(shape_list))
    return crop_json


class TestTransformUtils(unittest.TestCase):
    """test_transform_crop_ options"""

    @classmethod
    def setUpClass(cls):
        cls.image_ = cv2.imread("samples/solar.jpeg")
        cls.json_dict_ = read_json("samples/solar.json")
        cls.crop_cntr_ = cls.json_dict_["shapes"][0]["points"]
        # UI based ROI selection
        # cls.crop_cntr_ = select_roi_expanded(cls.image_, x_expn_fact=0, y_expn_fact=0)
        # print('cls.crop_cntr_:',cls.crop_cntr_)

    @classmethod
    def tearDownClass(cls):
        # cv2.namedWindow("Cropped", cv2.WINDOW_GUI_NORMAL)
        # cv2.imshow("Cropped", self.crop_image_)
        # cv2.waitKey(0)
        print("teardown")

    def trapezoid_crop_wrapper(self, write_name, h1=None, w1=None, pad_l=0, pad_r=0, pad_t=0, pad_b=0, expand_dest=True, crop_type="trapezoid", expected_shape=(), compare_img_flag=False, compare_json_flag=False, label_list=()):
        """wrapper for trapezoid crop"""
        crop_image_, crop_mask_, crop_json_, tr_ = transform_crop(
            image=self.image_,
            crop_cntr=self.crop_cntr_,
            mask=None,
            json_dict=self.json_dict_,
            crop_type=crop_type,
            h1=h1,
            w1=w1,
            pad_l=pad_l,
            pad_r=pad_r,
            pad_t=pad_t,
            pad_b=pad_b,
            tr=None,
            interpolation=cv2.INTER_CUBIC,
            expand_dest=expand_dest,
            label_list=label_list,
        )
        makedirs("samples/test_results", exist_ok=True)
        cv2.imwrite("samples/test_results/" + write_name + ".jpg", crop_image_)
        write_label_json("samples/test_results/" + write_name + ".json", crop_json_, image_path=write_name + ".jpg")
        assert crop_image_.shape == expected_shape, f"Expected crop shape is {expected_shape}, got {crop_image_.shape}"
        if compare_img_flag:
            compare_imgs("samples/test_results/" + write_name + ".jpg", "samples/transform_test/" + write_name + ".jpg")
        if compare_json_flag:
            compare_json("samples/test_results/" + write_name + ".json", "samples/transform_test/" + write_name + ".json")
        return crop_image_, crop_mask_, crop_json_, tr_

    def test_transform_crop_with_expand_destination(self):
        """Demo of transform_crop with expand_destination"""
        crop_image_, _, crop_json_, tr_ = self.trapezoid_crop_wrapper(h1=200, w1=200, pad_l=100, pad_r=100, pad_t=100, pad_b=100, expand_dest=True, crop_type="trapezoid", write_name="crop_image1", expected_shape=(400, 400, 3), compare_img_flag=True)

    def test_transform_crop_wo_expand_destination(self):
        """Demo of transform_crop with expand_destination"""
        crop_image_, _, crop_json_, tr_ = self.trapezoid_crop_wrapper(h1=200, w1=200, pad_l=50, pad_r=50, pad_t=50, pad_b=50, expand_dest=False, crop_type="trapezoid", write_name="crop_image2", expected_shape=(200, 200, 3), compare_img_flag=True)

    def test_transform_crop_wo_any_expansion(self):
        """Demo of transform_crop with expand_destination"""
        crop_image_, _, crop_json_, tr_ = self.trapezoid_crop_wrapper(h1=200, w1=200, expand_dest=False, crop_type="trapezoid", write_name="crop_image3", expected_shape=(200, 200, 3), compare_img_flag=True, compare_json_flag=True)

    def test_transform_crop_wo_any_expansion_wo_resize(self):
        """Demo of transform_crop with expand_destination"""
        crop_image_, _, crop_json_, tr_ = self.trapezoid_crop_wrapper(h1=None, w1=None, expand_dest=False, crop_type="trapezoid", write_name="crop_image4", expected_shape=(411, 488, 3), compare_img_flag=False)

    def test_bbox_crop(self):
        """Demo of transform_crop"""
        # self.json_dict_ = read_json("samples/Scopito_1.json")
        # self.crop_cntr_ = self.json_dict_["shapes"][4]["points"]
        crop_image_, _, crop_json_, tr_ = self.trapezoid_crop_wrapper(h1=None, w1=None, expand_dest=False, crop_type="bbox", write_name="crop_image5", expected_shape=(359, 828, 3), compare_img_flag=False)

    def test_fitbox_crop(self):
        """Demo of fitbox crop"""
        crop_image_, _, crop_json_, tr_ = self.trapezoid_crop_wrapper(h1=None, w1=None, expand_dest=False, crop_type="fitbox", write_name="crop_image6", expected_shape=(291, 866, 3), compare_img_flag=False)

    def test_fitbox_crop_crack_w_pad(self):
        """Demo of fitbox crop"""
        self.image_ = cv2.imread("samples/Scopito_1.JPG")
        self.json_dict_ = read_json("samples/Scopito_1.json")
        self.crop_cntr_ = self.json_dict_["shapes"][9]["points"]
        crop_image_, _, crop_json_, tr_ = self.trapezoid_crop_wrapper(
            h1=None, w1=None, pad_l=10, pad_r=10, pad_t=10, pad_b=10, expand_dest=False, crop_type="fitbox", write_name="crop_image7", expected_shape=(201, 14, 3), label_list=["A3_scopito_fiber"], compare_img_flag=True, compare_json_flag=True
        )

    def test_transform_paste(self):
        """test transform paste"""
        cleanup_json_dict = cleanup_json(json_dict=self.json_dict_, delete_labels=["cell"])
        write_name = "clean_solar"
        cv2.imwrite("samples/test_results/" + write_name + ".jpg", self.image_)
        write_label_json("samples/test_results/" + write_name + ".json", cleanup_json_dict, image_path=write_name + ".jpg")

        crop_json_dict = read_json("samples/transform_test/crop_image3.json")

        full_json = transform_paste(full_json_dict=cleanup_json_dict, crop_json_dict=crop_json_dict, label_list=["cell"])
        write_name = "new_solar"
        cv2.imwrite("samples/test_results/" + write_name + ".jpg", self.image_)
        write_label_json("samples/test_results/" + write_name + ".json", full_json, image_path=write_name + ".jpg")
        compare_json("samples/transform_test/" + write_name + ".json", "samples/test_results/" + write_name + ".json")

    def test_get_box(self, show_flag=False):
        """test if the box is coming correct"""
        print("contour:", self.crop_cntr_)
        box = get_box(self.crop_cntr_, crop_type="bbox")
        img = draw_cntrs(contours=[box], img=self.image_)  # type: ignore
        print("bbox\n", box)
        if show_flag:
            icv.show(img, time=0)
        assert get_contour_area(box) == 359 * 828, f"got {get_contour_area(box)}"
        box = get_box(self.crop_cntr_, crop_type="trapezoid")
        print("trapezoid\n", box)
        assert round(get_contour_area(box)) == 131719, f"got {get_contour_area(box)}"
        box = get_box(self.crop_cntr_, crop_type="fitbox")
        print("fit box\n", box)
        assert round(get_contour_area(box)) == 252202, f"got {get_contour_area(box)}"


if __name__ == "__main__":
    test_obj = TestTransformUtils()
    test_obj.setUpClass()
    test_obj.test_get_box(show_flag=False)
    test_obj.test_transform_crop_with_expand_destination()
    test_obj.test_transform_crop_wo_expand_destination()
    test_obj.test_transform_crop_wo_any_expansion()
    test_obj.test_transform_crop_wo_any_expansion_wo_resize()
    test_obj.test_bbox_crop()
    test_obj.test_fitbox_crop()
    test_obj.test_transform_paste()
    test_obj.test_fitbox_crop_crack_w_pad()

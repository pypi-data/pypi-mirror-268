""" Geometry operations based on point, line, trianlge"""
import unittest
import cv2
from sympy import Point, Line
import numpy as np
import shapely.geometry as geom
import math

def get_cartesian(lat = None,lon = None):
    '''
    Function converts a given latitude and longitude to cartesian coordinates
    '''
    lat, lon = np.deg2rad(lat), np.deg2rad(lon)
    R = 6371000 # radius of the earth
    x = R * np.cos(lat) * np.cos(lon)
    y = R * np.cos(lat) * np.sin(lon)
    z = R * np.sin(lat)

    return x,y,z

def get_lat_long(x, y, z):
    '''
    Function converts a given  cartesian coordinates to latitude and longitude
    '''
    R = 6371000
    lat = np.degrees(np.arcsin(z/R))
    lon = np.degrees(np.arctan2(y, x))

    return lat, lon


def euclidean_distance(pts1, pts2):
    '''
    This function returns eclidean distance between 2 points
    '''
    x1,y1,z1 = pts1[0], pts1[1], pts1[2]
    x2,y2,z2 = pts2[0], pts2[1], pts2[2]

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def euclidean(pt1, pt2):
    """Returns the euclidean distance between two points"""
    return np.sqrt(np.square(pt1[0] - pt2[0]) + np.square(pt1[1] - pt2[1]))


def line_intersection(line1_pt1, line1_pt2, line2_pt1, line2_pt2):
    """Returns the intersection point of two line segments"""
    p_1, p_2, p_3, p_4 = Point(line1_pt1), Point(line1_pt2), Point(line2_pt1), Point(line2_pt2)
    l_1 = Line(p_1, p_2)
    l_2 = Line(p_3, p_4)
    intersect = l_1.intersection(l_2)
    return [intersect[0][0], intersect[0][1]]

# pylint: disable=no-member
def get_nearest_pt(coords, pt):
    """Returns nearest point from pt to polyline joining coords"""  
    line = geom.LineString(coords)
    point = geom.Point(pt)
    # Note that "line.distance(point)" would be identical
    point_on_line = line.interpolate(line.project(point))
    # distance = self.line.distance(point)
    if point_on_line._ndim == 2:
        return [point_on_line.x, point_on_line.y]
    return [point_on_line.x, point_on_line.y, point_on_line.z]


def get_unit_vec(pt1, pt2):
    """Returns the unit vector"""
    direction_vec = (pt2[0] - pt1[0], pt2[1] - pt1[1])
    assert get_magnitude(direction_vec) != 0, "Magnitude of direction vector is zero"
    unit_vec = direction_vec / get_magnitude(direction_vec)
    # else:
    #     unit_vec = direction_vec
    return tuple(unit_vec)


def get_magnitude(pt):
    """Returns the magnitude of a vector"""
    magnitude = euclidean(pt, (0, 0))
    return magnitude


def get_slope(start_pt, end_pt):
    """Returns the slope of a line from two points"""
    slope = np.arctan2(end_pt[1] - start_pt[1], end_pt[0] - start_pt[0])
    return slope


def get_rotation_matrix(angle, c_x, c_y):
    """Returns the rotation matrix"""
    m = cv2.getRotationMatrix2D((c_x, c_y), -angle, 1.0)
    return m


def get_translation_matrix(t_x, t_y):
    """Returns the translation matrix"""
    m = np.float32([[1, 0, t_x], [0, 1, t_y]])
    return m


class TestGeomUtils(unittest.TestCase):
    """Unit test function created to check the pointutils"""

    def test_get_catesian(self):
        lat_ = -17.79619768
        long_ = -50.62608241
        x, y, z = get_cartesian(lat_, long_)
        self.assertListEqual([round(x, 3), round(y, 3), round(z, 3)], [3848233.439, -4689266.657, -1947182.225])

    def test_get_nearest_pt(self):
        """checks that `get_nearest_pt` returns the expected nearest point
        on a line given a set of coordinates and a point"""
        coords = [[0, 0], [10, 0]]
        pt = [5, 5]
        print("pt:", pt)
        print("coords:", coords)
        line = geom.LineString(coords)
        point = geom.Point(pt[0], pt[1])

        point_on_line = get_nearest_pt(coords, pt)
        print("shortest distance point_on_line:", point_on_line)
        self.assertListEqual(point_on_line, [5.0, 0.0])

    def test_line_intersection(self):
        """checks that `line_intersection` returns the expected intersection
        point between two lines given their endpoints"""
        line1_pt1 = [0, 0]
        line1_pt2 = [10, 0]
        line2_pt1 = [5, -5]
        line2_pt2 = [5, 5]
        print("line1_pt1:", line1_pt1, "line1_pt2:", line1_pt2)
        print("line2_pt1:", line2_pt1, "line2_pt2:", line2_pt2)
        pt = line_intersection(line1_pt1, line1_pt2, line2_pt1, line2_pt2)
        print("lines intersection point:", pt)
        self.assertListEqual(pt, [5.0, 0.0])

    def test_euclidean(self):
        """test checks that `euclidean` returns the expected Euclidean distance
        between two points"""
        assert euclidean(pt1=[0, 0], pt2=[10, 0]) == 10


if __name__ == "__main__":
    test_obj = TestGeomUtils()
    test_obj.test_get_nearest_pt()
    test_obj.test_line_intersection()

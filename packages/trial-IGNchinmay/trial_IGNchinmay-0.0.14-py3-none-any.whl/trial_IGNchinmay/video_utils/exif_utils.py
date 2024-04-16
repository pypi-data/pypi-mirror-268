# --------------------------------------------------------------------------
#                         Copyright © by
#           Ignitarium Technology Solutions Pvt. Ltd.
#                         All rights reserved.
#  This file contains confidential information that is proprietary to
#  Ignitarium Technology Solutions Pvt. Ltd. Distribution,
#  disclosure or reproduction of this file in part or whole is strictly
#  prohibited without prior written consent from Ignitarium.
# --------------------------------------------------------------------------
#  Filename    : exif_utils.py
# --------------------------------------------------------------------------
#  Description :
# --------------------------------------------------------------------------
"""To get the GPS data from the video."""

import json
import sys
import lsb_release_ex

from trial_IGNchinmay.draw_utils import print_colored
from trial_IGNchinmay.system_utils import subprocess_cmd


def get_metadata(video_path, fmt_file=None):
    """To get the GPS metadata from the video file.
    fmt_file: file, which we can provide, to perform the extraction
    This function is used to get the EXIF metadata from the video file.
    exif_file_info: dictionary containing the EXIF metadata.
    format sample: {
                    'SourceFile': 'sample_videos/set1/right/20211109_030954_NF_DriverRear.mp4',
                    'ExifToolVersion': 11.88,
                    'FileName': '20211109_030954_NF_DriverRear.mp4',
                    'Video Frame Rate': 9.99
                   }

    Args:
        video_path (str): Video path
        fmt_file (str, optional): Video file format, defaults to None

    Returns:
        str, str: exif_file_info: dictionary containing the EXIF
        metadata and gps_data
    """
    ubuntu_ver = float(lsb_release_ex.get_lsb_information().get("RELEASE"))
    assert ubuntu_ver >= 20.04, "Exiftool requires Ubuntu version to be 20 or above to get gps data"

    gps_data = None
    exif_file_info = {}
    if fmt_file is not None:
        command = f"exiftool -n -ee -b -p {fmt_file} {video_path}"
        try:
            ret, metadata, error = subprocess_cmd(command)
            if not error:
                gps_data = metadata
            else:
                print("[!] GPS Metadata ERROR: ", error)
        except:
            print_colored("[!] Error using exiftool!", "red")
            sys.exit()

    ret, file_info, error1 = subprocess_cmd(f"exiftool -json {video_path}")
    if not error1:
        exif_file_info = json.loads(file_info.strip())[0]
    return exif_file_info, gps_data

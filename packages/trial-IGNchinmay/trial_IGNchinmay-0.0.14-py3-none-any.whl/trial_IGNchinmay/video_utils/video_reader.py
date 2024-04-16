"""allows reading of video files using OpenCV. It is a versatile implementation that provides threading support to reduce input-output latency
when processing frames with computationally expensive transformations, and it allows access to the video frames using a frame number as the index"""
# import the necessary packages
import unittest
import time
import os
from queue import Queue
from threading import Thread
import cv2

from trial_IGNchinmay.draw_utils import print_colored
from trial_IGNchinmay.file_utils import get_file_name
from trial_IGNchinmay.typehint_utils import Mat


class VideoReader:
    """Video reader class that supports thread"""

    def __init__(self, path, frame_count=None, start_frame=0, transform=False, queue_size=20, keep_raw_frame=False, use_threading=False, queue_frame_skip=False):
        # initialize the file video stream along with the boolean
        # used to indicate if the thread should be stopped or not
        self.init_frame = start_frame
        self.frame_num = start_frame
        self.use_threading = use_threading
        self.keep_raw_frame = keep_raw_frame
        self.cap = cv2.VideoCapture(path)
        self.file_name = get_file_name(path)
        self.watch_q = Queue(maxsize=1)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.stopped = False
        self.transform = transform
        self.org_frame = None
        self.ret = None
        if frame_count:
            self.frame_count = frame_count
        else:
            self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if self.transform:
            self.keep_raw_frame = True
        self.queue_frame_skip = queue_frame_skip
        if self.queue_frame_skip:
            queue_size = 1
        self.que = Queue(maxsize=queue_size)
        if use_threading:
            # intialize thread
            self.thread = Thread(target=self.update, args=(lambda: self.stopped,))
            self.thread.daemon = True
        self.total_frame_count = int(self.frame_count)

    def start(self):
        """Starts the video stream thread"""
        if self.use_threading:
            self.thread.start()

    def get_height(self):
        """Returns the height of the video frame"""
        return int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_width(self):
        """Returns the width of the video frame"""
        return int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    def get_dimension(self):
        """Get height and width of the video"""
        height = self.get_height()
        width = self.get_width()
        return height, width

    def get_fps(self):
        """Get the FPS"""
        return self.fps

    def get_total_frames(self):
        """Total frame count"""
        return self.total_frame_count

    def preprocess(self, frame):
        """Custom preprocess func to override"""
        crop, crop_wo_seam, trans_mat = None, None, None
        return crop, crop_wo_seam, trans_mat

    def que_clear(self):
        """To clear the queue"""
        while not self.que.empty():
            try:
                self.que.get(block=False)
            except:
                continue
            self.que.task_done()

    def update(self, stop):
        """continuously reads frames from the video file and puts them into the queue until the end of the file or
        until `stop()` returns True"""
        # keep looping infinitely
        counter = 0
        while True:
            start_time = time.time()
            if self.watch_q.qsize():
                print("Reader stopping", self.init_frame)
                break
            frame = None
            if counter >= self.frame_count:
                break

            if stop() is True:
                print("Thread stop called!", self.init_frame)
                break

            # otherwise, ensure the queue has room in it
            if self.queue_frame_skip is False and self.que.full():
                time.sleep(0.1)
                continue

            # read the next frame from the file
            frame_num = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            (grabbed, frame) = self.cap.read()
            # if the `grabbed` boolean is `False`, then we have
            # reached the end of the video file
            if not grabbed:
                self.stopped = True
                self.que.put("EOF")
                break

            if (frame is None) or (len(frame.shape) != 3):
                print("Frame came empty, check.")
                continue

            if self.transform:
                processed_frame1, processed_frame2, trans_mat = self.preprocess(frame.copy())
                processed_frame = processed_frame1
                if processed_frame is None:
                    processed_frame = processed_frame2
            else:
                processed_frame = None
                trans_mat = None

            # add the frame to the queue
            if self.keep_raw_frame is None:
                frame = None

            if self.queue_frame_skip:
                self.que_clear()

            self.que.put([frame, processed_frame, trans_mat, frame_num])
            counter += 1
            time_spent = time.time() - start_time
            sleep_time = 0.25 - time_spent
            if self.queue_frame_skip and sleep_time > 0:
                time.sleep(sleep_time)

    def _read(self, frame_num):
        """Read the frames from the video threading/non-threading"""
        if self.use_threading:
            # return next frame in the queue
            output = self.que.get()
            frame_time = time.time()
            if output == "EOF":
                return "EOF", "EOF", "EOF", "EOF",  "EOF"
            if self.keep_raw_frame:
                org_frame, processed_frame, trans_mat, frame_num = output
            else:
                _, processed_frame, trans_mat, frame_num = output
                org_frame = None

        else:  # Directly reading from video capture object
            ret = False
            if frame_num == self.frame_num + 1 or self.org_frame is None:
                frame_num = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
                ret, org_frame = self.cap.read()
                frame_time = time.time()
                self.ret, self.org_frame = ret, org_frame
            elif frame_num == self.frame_num:
                ret, org_frame = self.ret, self.org_frame
            if not ret:
                self.que.put("EOF")
                return "EOF", "EOF", "EOF", "EOF", "EOF"
            if self.transform:
                processed_frame1, processed_frame2, trans_mat = self.preprocess(org_frame.copy())
                processed_frame = processed_frame1
                if processed_frame is None:
                    processed_frame = processed_frame2
            else:
                processed_frame = None
                trans_mat = None
            if self.keep_raw_frame is None:
                org_frame = None
        self.frame_num = int(frame_num)
        return org_frame, processed_frame, self.frame_num, trans_mat, frame_time

    def get_frame(self, frame_num: int) -> Mat:
        """get frame from video"""
        if not frame_num in (self.frame_num + 1, self.frame_num):
            self.set_framenum(frame_num)
        org_frame, processed_frame, frame_num_, trans_mat, frame_time = self._read(frame_num)
        if isinstance(org_frame, str) and org_frame == "EOF" and self.frame_num >= self.total_frame_count:
            return None, None, None, None, None
        if self.queue_frame_skip is False:
            assert frame_num_ == frame_num, "Reader frame number mismatch"
        return org_frame, processed_frame, frame_num_, trans_mat, frame_time

    def set_framenum(self, frame_num=0):
        """set cap to a specific frame number"""
        print(f"Setting frame number to {frame_num}")
        if self.use_threading:
            raise Exception("Set framenum feature supporting on Non-threaded mode")  # pylint: disable=W0719
        if frame_num > self.frame_count or frame_num < 0:
            print_colored("[!] Error! frame_num > self.total_frame_count or frame_num<0", "red")
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        self.frame_num = frame_num
        self.org_frame = None
        self.ret = None

        return True

    def running(self):
        """Checks if the video stream is still running"""
        return self.more() or not self.stopped

    def more(self):
        """Checks if there are more frames in the video stream queue"""
        # return True if there are still frames in the queue. If stream is not stopped, try to wait a moment
        tries = 0
        while self.que.qsize() == 0 and not self.stopped and tries < 5:
            time.sleep(0.1)
            tries += 1

        return self.que.qsize() > 0

    def stop(self):
        """Stop the thread and the video stream."""
        if self.use_threading:
            # indicate that the thread should be stopped
            self.stopped = True
            try:
                self.watch_q.put("STOP", block=False)
                self.thread.join()
                self.cap.release()
            except:
                pass
            count = 0
            while count < 10:
                if self.thread.is_alive():
                    time.sleep(0.1)
                    count += 1
                else:
                    break
            # print("End Of Thread", self.init_frame)
            # wait until stream resources are released (producer thread might be still grabbing frame)

    def __del__(self):
        self.stop()


class TransformTest(VideoReader):
    """Testing transform method in video reader"""

    def __init__(self, video_path, preprocess_mode):
        super().__init__(path=video_path, transform=preprocess_mode)

    def preprocess(self, frame):
        """Transform method applied to all frames"""
        gray_img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        return gray_img, None, None


class TestVideoReader(unittest.TestCase):
    """Test methods"""

    def test_without_threading(self):
        """Testing video reader without threading"""
        video_path = os.path.join("samples", "video_utils_test", "sample.mp4")
        write_path = os.path.join("samples", "video_utils_test", "results")
        start_frame = 0
        reader_obj = VideoReader(video_path, start_frame=start_frame, use_threading=False)
        frame_no = start_frame
        total_frame_cnt = reader_obj.get_total_frames()
        for _ in range(total_frame_cnt):
            org_frame, processed_frame, frame_num_, trans_mat, _ = reader_obj.get_frame(frame_no)
            if org_frame is None:
                break
            frame_no += 1
            cv2.imwrite(f"{write_path}/{frame_no}.jpg", org_frame)
        assert frame_no == 5, "Video reader without threading test failed"

    def test_with_threading(self):
        """Testing video reader with threading"""
        video_path = os.path.join("samples", "video_utils_test", "sample.mp4")
        write_path = os.path.join("samples", "video_utils_test", "results")
        start_frame = 0
        reader_obj = VideoReader(video_path, start_frame=start_frame, keep_raw_frame=True, use_threading=True)
        reader_obj.start()
        frame_no = start_frame
        total_frame_cnt = reader_obj.get_total_frames()
        for _ in range(total_frame_cnt):
            org_frame, processed_frame, frame_num_, trans_mat, _ = reader_obj.get_frame(frame_no)
            if org_frame is None:
                break
            cv2.imwrite(f"{write_path}/{frame_no}.jpg", org_frame)
            frame_no += 1
        reader_obj.stop()
        assert frame_no == 5, "Video reader with threading test failed"

    def test_with_transform(self):
        """Testing video reader with transform"""
        video_path = os.path.join("samples", "video_utils_test", "sample.mp4")
        write_path = os.path.join("samples", "video_utils_test", "results")
        reader_obj = TransformTest(video_path, preprocess_mode=True)
        frame_no = 0
        total_frame_cnt = reader_obj.get_total_frames()
        for _ in range(total_frame_cnt):
            org_frame, processed_frame, frame_num_, trans_mat, _ = reader_obj.get_frame(frame_no)
            if org_frame is None:
                break
            cv2.imwrite(f"{write_path}/{frame_no}.jpg", org_frame)
            cv2.imwrite(f"{write_path}/transformed_{frame_no}.jpg", processed_frame)
            frame_no += 1
        assert frame_no == 5, "Video reader with transform test failed"


if __name__ == "__main__":
    test_obj = TestVideoReader()
    test_obj.test_without_threading()
    test_obj.test_with_threading()
    test_obj.test_with_transform()

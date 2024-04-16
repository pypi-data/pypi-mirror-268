""" Multiprocess base class to inherit and use"""

import multiprocessing as mp
import time
import unittest

import logging


class BaseProcess(mp.Process):
    """A process backed by an internal queue
    for simple one-way message passing.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = mp.Queue()
        self.daemon = True
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger()

    def send(self, msg):
        """Puts msg in queue"""
        self.queue.put(msg)

    def stop(self):
        """Stop process"""
        self.queue.put("stop")
        # self.join()

    def on_stop(self):
        """call on stop"""

    def do_func(self, msg):
        """do something"""
        # self.logger.info(msg)

    def run(self):
        """this loop starts on calling start()"""
        while True:
            if not self.queue.empty():
                msg = self.queue.get()
                if msg == "stop":
                    print("Stopping process")
                    break
                self.do_func(msg)
            else:
                time.sleep(0.25)
        self.on_stop()


class MyProcess(BaseProcess):
    """text print example"""

    def do_func(self, txt):
        time.sleep(1)
        self.logger.info("From child process: %s",txt)

    def on_stop(self):
        print("on stop override")


class TestmultiProcessUtils(unittest.TestCase):
    """test mult process utils"""

    def test_mutli_process(self):
        """test multi process inheritance"""
        process = MyProcess()
        process.start()

        txts = [1, 2, 3, 4, 5]
        for txt_ in txts:
            process.send(txt_)
        print("Items put in que for child process to execute")
        print("Main thread is free to do something else now!")
        for txt_ in txts:
            print("From main:", txt_)
        time.sleep(6)
        print("Stopping process")
        process.stop()


if __name__ == "__main__":
    test_obj = TestmultiProcessUtils()
    test_obj.test_mutli_process()

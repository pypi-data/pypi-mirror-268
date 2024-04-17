import time
import inspect
from typing import Dict, List


class Timer(object):
    storedSecs: Dict[str, Dict[str, List[float]]] = {}  # Class variable

    def __init__(self, title: str, enalbe: bool = True):
        self.title = title
        self.enable = enalbe

        if self.enable is False:
            return

        self.maxStores = 1

        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame, 2)
        frame = caller_frame[1]
        filename = frame.filename
        line_number = frame.lineno
        self.key = f"{filename}_{line_number}_{title}"
        if self.key not in self.storedSecs:
            self.storedSecs[self.key] = {}

    def __enter__(self):
        if self.enable is False:
            return self
        self.current = time.time()
        self.start = time.time()
        return self

    def record(self, lapname: str):
        if self.enable is False:
            return
        self.lapkey = f"{self.key}_{lapname}"
        prev = self.current
        self.current = time.time()
        if self.lapkey not in self.storedSecs[self.key]:
            self.storedSecs[self.key][self.lapkey] = []
        self.storedSecs[self.key][self.lapkey].append(self.current - prev)
        self.storedSecs[self.key][self.lapkey] = self.storedSecs[self.key][self.lapkey][-self.maxStores :]

    def __exit__(self, *_):
        if self.enable is False:
            return
        self.end = time.time()
        self.elapsed = (self.end - self.start) * 1000
        print(f"---- {self.title}(elapsed:{round(self.elapsed,1)}ms) ----")
        for key, val in self.storedSecs[self.key].items():
            section = key.split("_")[-1]
            milisecAvr = sum(val) / len(val) * 1000
            print(f"{section}: {round(milisecAvr,1)} msec, {val[-1]}")

"""
Helpers for progress bars and ETA estimation.
"""

import time

from .logs import logger

log = logger(__file__)
# ----------------------------------------------------------
# Progress
# ----------------------------------------------------------
class Progress:
    "A class to measure the progress of an algorithm"

    def __init__(self, x0=0, N=10, label=''):
        self.n0 = 0
        self.n1 = 0
        self.x = x0
        self.N = N
        self.samples = []
        self.t0 = 0
        self.t1 = 0
        self.freq = 5
        self.data = {}
        self.label = label

    def set(self, x, force=False, **data):
        "Set the progress"
        self.x = x
        self._step(force, **data)

    def update(self, n=1, force=False, **data):
        "Update the progress"
        self.x += n
        self.n1 += n
        self._step(force, **data)

    def _step(self, force=False, **data):
        "Update the progress"
        t1 = time.time()
        self.data.update(data)
        sample = t1, self.x
        
        self.samples.append(sample)
        if len(self.samples) > 200:
            self.samples = self.samples[100:]

        if force or t1 > self.t1:
            elapsed = t1 - self.t0
            speed = self.n1 / elapsed
            self.t0 = t1
            self.t1 = t1 + self.freq
            self.n1 = 0
            log.info(f"[{self.label}] Speed: {speed:.2f} items/sec: {self.data}: {self.x}")

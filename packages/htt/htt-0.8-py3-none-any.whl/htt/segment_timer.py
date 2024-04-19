import time
from typing import List

from dataclasses import dataclass


@dataclass
class Segment:
    name: str = None
    start_time: float = None
    stop_time: float = None
    duration: float = None


class SegmentTimer:
    def __init__(
        self,
    ):
        self._segments = []
        self._current_segment = None

    def get_segments(
        self,
    ) -> List[Segment]:
        return self._segments

    def reset(
        self,
    ):
        self._segments = []
        self._current_segment = None

    def start_segment(
        self,
    ):
        assert not self._current_segment
        current_time = time.time()
        self._current_segment = Segment(start_time=current_time)

    def split_segment(
        self,
        name: str,
    ):
        assert self._current_segment
        current_time = time.time()
        self._current_segment.stop_time = current_time
        self._current_segment.duration = current_time - self._current_segment.start_time
        self._current_segment.name = name
        self._segments.append(self._current_segment)
        self._current_segment = Segment(start_time=self._current_segment.start_time)

    def stop_segment(
        self,
        name: str,
    ):
        assert self._current_segment
        current_time = time.time()
        self._current_segment.stop_time = current_time
        self._current_segment.duration = current_time - self._current_segment.start_time
        self._current_segment.name = name
        self._segments.append(self._current_segment)
        self._current_segment = None

    def next_segment(
        self,
        name: str,
    ):
        assert self._current_segment
        current_time = time.time()
        self._current_segment.stop_time = current_time
        self._current_segment.duration = current_time - self._current_segment.start_time
        self._current_segment.name = name
        self._segments.append(self._current_segment)
        self._current_segment = Segment(start_time=current_time)

from typing import Optional

from . import _exceptions


class Sequence(object):
    @classmethod
    def for_request_id(cls):
        return cls(initial=0, max_value=2**32, delta=2)

    @classmethod
    def for_stream_id(cls):
        return cls(initial=1, max_value=2**32, delta=1)

    @classmethod
    def for_sequence_number(cls):
        return cls(initial=1, max_value=2**32, delta=1, is_cyclic=False)

    @classmethod
    def for_ack_id(cls):
        return cls(initial=1, max_value=2**32, delta=1)

    @classmethod
    def for_data_id_alias(cls):
        return cls(initial=1, max_value=2**32, delta=1)

    @classmethod
    def for_upstream_info_alias(cls):
        return cls(initial=1, max_value=2**32, delta=1)

    def __init__(self, initial: int, max_value: int, delta: int, is_cyclic=True):
        self._next = initial
        self._current: Optional[int] = None
        self._max_value = max_value
        self._delta = delta
        self._is_cyclic = is_cyclic

    def __call__(self) -> int:
        res = self._next
        self._current = res
        if not self._is_cyclic and self._current > self._max_value:
            raise _exceptions.ISCPException(message=f"exceeded max value max={self._max_value}")
        self._next = (self._next + self._delta) % self._max_value
        return res

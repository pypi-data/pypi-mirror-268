from abc import ABC, abstractmethod
from ..sq_object import SQObject
from ..sq_packet import SQPacket


class SQQueue(SQObject):

    def pop(self, **kwargs):
        self.collect_statistics()

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def peek(self):
        pass

    def push(self, pkt: SQPacket):
        self.collect_statistics()

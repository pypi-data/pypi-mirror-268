from typing import Generator, List, Union
import numpy as np
from ...sq_packet import SQPacket, SQMetadata
from ...sq_queue import SQQueue
from ...sq_event import SQEvent
from ..sq_helper import SQHelper
from .sq_packet_info import SQPacketInfo
from .sq_generic_packet import SQGenericPacket
from ...sq_time_base import SQTimeBase


def register(helper_factory):
    helper_factory.register(name="default", factory=SQDefaultHelper)


class SQDefaultHelper(SQHelper):

    def __init__(self, data: dict[str, any]):
        super().__init__(data)
        self.pkt_size_mean = data.get('pkt_size_mean', 1000)
        self.pkt_size_sd = data.get('pkt_size_sd', 2000)
        self.classes = data.get('classes', ['A'])
        self.priorities = data.get('priorities', [1, 10])
        self.pkt_id_range = data.get('pkt_id_range', [1, 100])

    def generate_packets(self) -> Generator[SQPacket, None, None]:
        while True:
            pkt_size = int(np.abs(np.random.normal(self.pkt_size_mean, self.pkt_size_sd, None)))
            pkt_class = np.random.choice(self.classes, None)
            pkt_priority = np.random.randint(self.priorities[0], self.priorities[1], None)
            pkt_id = np.random.randint(self.pkt_id_range[0], self.pkt_id_range[1], None)
            yield SQGenericPacket(id=pkt_id,
                                  size=pkt_size,
                                  class_name=pkt_class,
                                  priority=pkt_priority,
                                  timestamp=SQTimeBase.get_current_sim_time())

    def get_processing_cycles(self, pkt: SQPacket) -> int:
        np.random.seed(pkt.size)
        return np.random.randint(1, 10)

    def process_packet(self, pkt: SQPacket, tick: int) -> bool:
        self.owner.logger.info(f'Processing packet {pkt} at tick {tick}')
        if tick < self.get_processing_cycles(pkt):
            return False
        return True

    def filter_packet(self, pkt: SQPacket) -> bool:
        return True

    def process_data(self, data: SQEvent, tick: int):
        self.owner.logger.info(f'Consuming Metadata {data}')

    def select_input_queue(self) -> Union[SQQueue, None]:
        if hasattr(self.owner, "input_qs"):
            q = self.owner.input_qs[self.q_idx]
            self.q_idx = (self.q_idx + 1) % len(self.owner.input_qs)
            return q
        else:
            return None

    def select_output_queue(self, pkt) -> Union[SQQueue, None]:
        if hasattr(self.owner, "output_qs"):
            q = self.owner.output_qs[self.q_idx]
            self.q_idx = (self.q_idx + 1) % len(self.owner.output_qs)
            return q
        else:
            return None

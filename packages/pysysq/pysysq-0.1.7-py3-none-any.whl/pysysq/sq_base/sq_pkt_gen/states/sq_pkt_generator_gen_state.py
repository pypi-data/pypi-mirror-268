from .sq_generator_state import SQPktGeneratorState
from ...sq_event import SQEvent


class SQPktGeneratorGenState(SQPktGeneratorState):
    def process_packet(self, evt: SQEvent):
        self.owner.logger.info(f'Generating Packet')
        pkt = next(self.owner.helper.generate_packets())
        if pkt is not None:
            self.owner.generated_pkts += 1
            self.owner.logger.info(f'Queuing Packet {pkt}')
            self.owner.output_q.push(pkt)

    def get_state_name(self):
        return f'GENERATING'

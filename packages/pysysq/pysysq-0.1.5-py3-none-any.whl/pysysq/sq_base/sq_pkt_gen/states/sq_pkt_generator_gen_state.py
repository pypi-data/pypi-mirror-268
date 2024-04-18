from .sq_generator_state import SQPktGeneratorState
from ...sq_event import SQEvent


class SQPktGeneratorGenState(SQPktGeneratorState):
    def process_packet(self, evt: SQEvent):
        self.owner.generated_pkts = 0
        self.owner.logger.info(f'Generating Packet')
        pkt = next(self.owner.helper.generate_packets())
        self.owner.output_q.push(pkt)

    def get_state_name(self):
        return f'GENERATING'

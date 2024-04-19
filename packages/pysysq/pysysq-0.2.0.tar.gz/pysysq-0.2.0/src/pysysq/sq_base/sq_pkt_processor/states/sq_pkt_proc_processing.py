from .sq_pkt_processor_state import SQPktProcState
from ...sq_event import SQEvent


class SQPktProcStateProcessing(SQPktProcState):
    def process_packet(self, evt: SQEvent):
        status = self.owner.helper.process_packet(self.owner.curr_pkt, self.owner.tick)

        if status:
            self.owner.set_state(self.factory.create_state('COMPLETE', owner=self.owner))
        else:
            self.owner.logger.info(f'{self.owner.name} Continue Processing Packet '
                                   f'{self.owner.curr_pkt}')

    def get_state_name(self):
        return f'PROCESSING'

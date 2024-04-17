import unittest
from unittest.mock import MagicMock
from dataclasses import dataclass
from ...src.pysysq import *
from ...src.pysysq.sq_base.sq_plugin.default.sq_generic_packet import SQGenericPacket


class TestSQDemux(unittest.TestCase):

    def setUp(self):
        self.factory = SQFactory()
        self.rx_q1 = self.factory.create('SQQueue', {'name': 'rx_q1', 'capacity': 10})
        self.rx_q2 = self.factory.create('SQQueue', {'name': 'rx_q2', 'capacity': 10})
        self.rx_q3 = self.factory.create('SQQueue', {'name': 'rx_q3', 'capacity': 10})
        self.rx_qs = [self.rx_q1, self.rx_q2, self.rx_q3]
        self.output_q = self.factory.create('SQQueue', {'name': 'input_q', 'capacity': 10})
        self.clk = self.factory.create('SQClock', {'name': 'clk', 'clk_divider': 1})

        self.mux = self.factory.create(obj_type='SQMux',
                                       data={
                                           'name': 'mux',
                                           'output_q': self.output_q,
                                           'input_qs': self.rx_qs,
                                           'clk': self.clk}
                                       )
        self.simulator = None

    def run_sim_loops(self, no_of_sim_loops: int):
        self.simulator = self.factory.create(obj_type='SQSimulator',
                                             data={
                                                 'name': 'simulator',
                                                 'max_sim_time': no_of_sim_loops,
                                                 'time_step': 0.1,
                                                 'children': [
                                                     self.clk,
                                                     self.mux,
                                                     self.rx_q1,
                                                     self.rx_q2,
                                                     self.rx_q3,
                                                     self.output_q
                                                 ]
                                             }
                                             )
        self.simulator.init()
        self.simulator.start()

    def test_mux_queue_selection(self):
        # Arrange

        self.rx_q1.push(SQGenericPacket(id=0))
        self.rx_q2.push(SQGenericPacket(id=10))
        self.rx_q3.push(SQGenericPacket(id=20))

        # Act
        self.run_sim_loops(no_of_sim_loops=4)

        # Assert
        for i in range(3):
            id = self.output_q.pop().id
            print(f'popped packet = {id}')
            self.assertEqual(id, i * 10)

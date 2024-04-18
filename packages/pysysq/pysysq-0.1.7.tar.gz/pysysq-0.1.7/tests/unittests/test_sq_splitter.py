import unittest
from unittest.mock import MagicMock
from dataclasses import dataclass
from ...src.pysysq import *
from ...src.pysysq.sq_base.sq_plugin.default.sq_generic_packet import SQGenericPacket


class TestSQDemux(unittest.TestCase):

    def setUp(self):
        self.factory = SQFactory()
        self.tx_q1 = self.factory.create('SQQueue', {'name': 'tx_q1', 'capacity': 10})
        self.tx_q2 = self.factory.create('SQQueue', {'name': 'tx_q2', 'capacity': 10})
        self.tx_q3 = self.factory.create('SQQueue', {'name': 'tx_q3', 'capacity': 10})
        self.tx_qs = [self.tx_q1, self.tx_q2, self.tx_q3]
        self.input_q = self.factory.create('SQQueue', {'name': 'input_q', 'capacity': 10})
        self.clk = self.factory.create('SQClock', {'name': 'clk', 'clk_divider': 1})

        self.splitter = self.factory.create(obj_type='SQSplitter',
                                            data={
                                                'name': 'splitter',
                                                'output_qs': self.tx_qs,
                                                'input_q': self.input_q,
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
                                                     self.splitter,
                                                     self.tx_q1,
                                                     self.tx_q2,
                                                     self.tx_q3,
                                                     self.input_q
                                                 ]
                                             }
                                             )
        self.simulator.init()
        self.simulator.start()

    def test_splitter(self):
        # Arrange

        self.input_q.push(SQGenericPacket(id=0))
        self.input_q.push(SQGenericPacket(id=10))
        self.input_q.push(SQGenericPacket(id=20))

        # Act
        self.run_sim_loops(no_of_sim_loops=4)

        # Assert
        for i in range(3):
            id = self.tx_q1.pop().id
            print(f'popped packet = {id}')
            self.assertEqual(id, i * 10)
        for i in range(3):
            id = self.tx_q2.pop().id
            print(f'popped packet = {id}')
            self.assertEqual(id, i * 10)
        for i in range(3):
            id = self.tx_q3.pop().id
            print(f'popped packet = {id}')
            self.assertEqual(id, i * 10)

import unittest


class TestHelper(unittest.TestCase):
    def check_next_line(self, strategy, result_list):
        strategy.read_line()
        strategy.plan_time_quantum()
        processor_state = strategy.get_processor_state()
        self.assertEqual(processor_state, result_list)

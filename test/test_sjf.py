import io
import sjf
import test.helpers as h


class TestSJF(h.TestHelper):
    def test_empty_line(self):
        PROCESSORS_NUM = 1
        input = io.StringIO("\n")
        strategy = sjf.SJF(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [-1])

    def test_one_processor_2procs(self):
        PROCESSORS_NUM = 1
        input = io.StringIO("0 1 0 2\n" +
                            "1 2 0 1\n")

        strategy = sjf.SJF(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1])
        self.check_next_line(strategy, [1])
        self.check_next_line(strategy, [2])

    def test_two_processors_4procs(self):
        PROCESSORS_NUM = 2
        input = io.StringIO("0 1 0 3 2 0 2 3 0 1\n" +
                            "1 4 0 1\n")

        strategy = sjf.SJF(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [3, 2])
        self.check_next_line(strategy, [2, 4])
        self.check_next_line(strategy, [1, -1])
        self.check_next_line(strategy, [1, -1])
        self.check_next_line(strategy, [1, -1])

    def test_three_processors_1proc(self):
        PROCESSORS_NUM = 3
        input = io.StringIO("0 1 0 1\n")

        strategy = sjf.SJF(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1, -1, -1])

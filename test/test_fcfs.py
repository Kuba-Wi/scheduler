import fcfs
import io
import test.helpers as h


class TestFCFS(h.TestHelper):
    def test_empty_line(self):
        PROCESSORS_NUM = 1
        input = io.StringIO("\n")
        strategy = fcfs.FCFS(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [-1])

    def test_one_processor_2procs(self):
        PROCESSORS_NUM = 1
        input = io.StringIO("0 1 0 2\n" +
                            "1 2 0 1\n")

        strategy = fcfs.FCFS(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1])
        self.check_next_line(strategy, [1])
        self.check_next_line(strategy, [2])

    def test_two_processors_3procs(self):
        PROCESSORS_NUM = 2
        input = io.StringIO("0 1 0 1 2 0 3\n" +
                            "1 3 0 2\n")

        strategy = fcfs.FCFS(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1, 2])
        self.check_next_line(strategy, [2, 3])
        self.check_next_line(strategy, [2, 3])

    def test_three_processors_1proc(self):
        PROCESSORS_NUM = 3
        input = io.StringIO("0 1 0 1\n")

        strategy = fcfs.FCFS(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1, -1, -1])


class TestSimplePriorityFcfs(h.TestHelper):
    def test_empty_line(self):
        PROCESSORS_NUM = 1
        input = io.StringIO("\n")
        strategy = fcfs.SimplePriorityFcfs(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [-1])

    def test_one_processor_2procs(self):
        PROCESSORS_NUM = 1
        input = io.StringIO("0 1 1 2\n" +
                            "1 2 0 1\n")

        strategy = fcfs.SimplePriorityFcfs(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1])
        self.check_next_line(strategy, [1])
        self.check_next_line(strategy, [2])

    def test_two_processors_3procs(self):
        PROCESSORS_NUM = 2
        input = io.StringIO("0 1 2 1 2 1 3\n" +
                            "1 3 0 2\n")

        strategy = fcfs.SimplePriorityFcfs(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [2, 1])
        self.check_next_line(strategy, [2, 3])
        self.check_next_line(strategy, [2, 3])

    def test_three_processors_1proc(self):
        PROCESSORS_NUM = 3
        input = io.StringIO("0 1 0 1\n")

        strategy = fcfs.SimplePriorityFcfs(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1, -1, -1])


class TestPriorityFcfsWithDispossess(h.TestHelper):
    def test_empty_line(self):
        PROCESSORS_NUM = 1
        input = io.StringIO("\n")
        strategy = fcfs.PriorityFcfsWithDispossess(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [-1])

    def test_one_processor_2procs(self):
        PROCESSORS_NUM = 1
        input = io.StringIO("0 1 1 2\n" +
                            "1 2 0 1\n")

        strategy = fcfs.PriorityFcfsWithDispossess(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1])
        self.check_next_line(strategy, [2])
        self.check_next_line(strategy, [1])

    def test_two_processors_3procs(self):
        PROCESSORS_NUM = 2
        input = io.StringIO("0 1 2 1 2 1 3\n" +
                            "1 3 0 2\n")

        strategy = fcfs.PriorityFcfsWithDispossess(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [2, 1])
        self.check_next_line(strategy, [3, 2])
        self.check_next_line(strategy, [3, 2])

    def test_three_processors_1proc(self):
        PROCESSORS_NUM = 3
        input = io.StringIO("0 1 0 1\n")

        strategy = fcfs.PriorityFcfsWithDispossess(PROCESSORS_NUM, input)

        self.check_next_line(strategy, [1, -1, -1])

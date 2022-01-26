import enum


class Schedule_state(enum.Enum):
    ONGOING = 0,
    FINISHED = 1


class Process:
    def __init__(self, pid, priority, time_left, start_time):
        self.pid = pid
        self.priority = priority
        self.time_left = time_left
        self.start_time = start_time

    @staticmethod
    def build_process(data):
        if len(data) != 4:
            return None

        return Process(data[0], data[1], data[2], data[3])


class Strategy:
    def __init__(self, processors_num):
        self.processors_num = processors_num
        self.current_time = -1
        self.process_list = []
        self.processor_process_dict = {i + 1 : None for i in range(0, self.processors_num)}
    
    def read_line(self) -> bool:
        line = input()
        if len(line) == 0:
            return False

        processes_data = line.split()
        start_time = processes_data.pop(0)
        i = 0
        while i + 3 <= len(processes_data):
            data = processes_data[i:i+3]
            data.append(start_time)
            proc = Process.build_process([int(i) for i in data])
            if proc:
                self.process_list.append(proc)
            i += 3

        return True

    def print_processor_state(self):
        print(str(self.current_time), end=' ')
        for proc in self.processor_process_dict.values():
            if proc:
                print(proc.pid, end=' ')
            else:
                print('-1 ', end=' ')
        print('')

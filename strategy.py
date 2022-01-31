import enum


class StrategyCode(enum.IntEnum):
    FCFS = 0,
    SJF = 1,
    SRTF = 2,
    ROUND_ROBIN = 3,
    PRIORITY_FCFS = 4,
    PRIORITY_SRTF = 5,
    PRIORITY_SIMPLE_FCFS = 6


class ScheduleState(enum.Enum):
    ONGOING = 0,
    FINISHED = 1


class Process:
    def __init__(self, pid, priority, time_left, start_time):
        self.pid = pid
        self.priority = priority
        self.time_left = time_left
        self.start_time = start_time

    @classmethod
    def build_from_list(cls, data):
        if len(data) != 4:
            return None

        return Process(data[0], data[1], data[2], data[3])


class Strategy:
    def __init__(self, processors_num):
        self._processors_num = processors_num
        self._current_time = -1
        self._process_list = []
        self._processor_process_dict = {
            i + 1: None for i in range(self._processors_num)}

    def read_line(self) -> bool:
        line = input()
        if not line:
            return False

        processes_data = line.split()
        start_time = processes_data.pop(0)

        for i in range(0, len(processes_data) + 1, 3):
            data = processes_data[i:i+3]
            data.append(start_time)
            proc = Process.build_from_list([int(i) for i in data])
            if proc:
                self._process_list.append(proc)

        return True

    def print_processor_state(self):
        print(str(self._current_time), end=' ')
        for proc in self._processor_process_dict.values():
            if proc:
                print(proc.pid, end=' ')
            else:
                print('-1 ', end='')
        print('')

    def _remove_finished_processes(self):
        self._process_list = [
            proc for proc in self._process_list if proc.time_left != 0]

    def _move_processes_to_lowest_free_processors(self):
        values = list(self._processor_process_dict.values())
        values.sort(key=lambda val: 0 if val else 1)

        for i in range(len(self._processor_process_dict.items())):
            self._processor_process_dict[i + 1] = values[i]


class SimpleStrategy(Strategy):
    def _plan_time_quantum(self, strategy_function) -> ScheduleState:
        self._current_time += 1
        for processor, proc in self._processor_process_dict.items():
            if proc:
                if proc.time_left == 0:
                    self._processor_process_dict[processor] = None
                else:
                    proc.time_left -= 1

        self._remove_finished_processes()
        self._move_processes_to_lowest_free_processors()
        busy_processors_num = self.__put_processes_on_free_processors(
            strategy_function)

        return ScheduleState.FINISHED if busy_processors_num == 0 else ScheduleState.ONGOING

    def __put_processes_on_free_processors(self, chose_process_to_put_on_processor) -> int:
        busy_processors_num = 0
        for processor, proc in self._processor_process_dict.items():
            if not proc:
                chosen_proc = chose_process_to_put_on_processor()
                if not chosen_proc:
                    return busy_processors_num

                chosen_proc.time_left -= 1
                self._processor_process_dict[processor] = chosen_proc
                busy_processors_num += 1
            else:
                busy_processors_num += 1

        return busy_processors_num


class StrategyWithDispossess(Strategy):
    def _plan_time_quantum(self, strategy_function) -> ScheduleState:
        self._current_time += 1
        for processor in self._processor_process_dict.keys():
            self._processor_process_dict[processor] = None

        self._remove_finished_processes()

        busy_processors_num = 0
        while busy_processors_num < len(self._processor_process_dict):
            chosen_proc = strategy_function()
            if not chosen_proc:
                break

            busy_processors_num += 1
            self._processor_process_dict[busy_processors_num] = chosen_proc

        for proc in self._processor_process_dict.values():
            if proc:
                proc.time_left -= 1

        return ScheduleState.FINISHED if busy_processors_num == 0 else ScheduleState.ONGOING

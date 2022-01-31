import sys
import strategy as s


class ProcRoundRobin(s.Process):
    def __init__(self, pid, priority, time_left, start_time):
        super().__init__(pid, priority, time_left, start_time)

        self.time_quantum_left = 0


class RoundRobin(s.Strategy):
    def __init__(self, processors_num, time_quantum, input_stream=sys.stdin):
        super().__init__(processors_num, input_stream)

        self._time_quantum = time_quantum

    def plan_time_quantum(self) -> s.ScheduleState:
        self._current_time += 1

        for processor, proc in self._processor_process_dict.items():
            if proc:
                if proc.time_left == 0:
                    self._processor_process_dict[processor] = None
                elif proc.time_quantum_left == 0:
                    self._process_list.remove(proc)
                    self._process_list.append(proc)
                    self._processor_process_dict[processor] = None
                else:
                    proc.time_left -= 1
                    proc.time_quantum_left -= 1

        self._remove_finished_processes()
        self._move_processes_to_lowest_free_processors()
        busy_processors_num = self.__put_processes_on_free_processors()

        return s.ScheduleState.FINISHED if busy_processors_num == 0 else s.ScheduleState.ONGOING

    def _chose_proc_to_put_on_processor(self):
        for proc in self._process_list:
            if (proc not in self._processor_process_dict.values()) and proc.time_left > 0:
                return proc

        return None

    def __put_processes_on_free_processors(self) -> int:
        busy_processors_num = 0
        for processor, proc in self._processor_process_dict.items():
            if not proc:
                chosen_proc = self._chose_proc_to_put_on_processor()
                if not chosen_proc:
                    return busy_processors_num

                chosen_proc.time_left -= 1
                chosen_proc.time_quantum_left = self._time_quantum - 1
                self._processor_process_dict[processor] = chosen_proc
                busy_processors_num += 1
            else:
                busy_processors_num += 1

        return busy_processors_num

import strategies as s

class FCFS(s.Strategy):
    def __init__(self, processors_num):
        super().__init__(processors_num)

    def plan_time_quantum(self) -> s.Schedule_state:
        self.current_time += 1
        for processor, proc in self.processor_process_dict.items():
            if proc:
                if proc.time_left == 0:
                    self.processor_process_dict[processor] = None
                else:
                    proc.time_left -= 1

        self.__move_processes_to_lowest_free_processors()
        busy_processors_num = self.__put_processes_on_free_processors()
        
        return s.Schedule_state.FINISHED if busy_processors_num == 0 else s.Schedule_state.ONGOING

    def put_new_process_on_processor(self, processor) -> s.Process:
        best_proc = None
        for proc in self.process_list:
            if (proc not in self.processor_process_dict.values()) and proc.time_left > 0:
                if not best_proc:
                    best_proc = proc
                elif proc.start_time < best_proc.start_time:
                    best_proc = proc
                elif proc.start_time == best_proc.start_time:
                    if proc.priority < best_proc.priority:
                        best_proc = proc
        
        self.processor_process_dict[processor] = best_proc
        return self.processor_process_dict[processor]

    def __put_processes_on_free_processors(self) -> int:
        busy_processors_num = 0
        for processor, proc in self.processor_process_dict.items():
            if not proc:
                added_proc = self.put_new_process_on_processor(processor)
                if added_proc:
                    added_proc.time_left -= 1
                    busy_processors_num += 1
            else:
                busy_processors_num += 1
        
        return busy_processors_num

    def __move_processes_to_lowest_free_processors(self):
        values = list(self.processor_process_dict.values())
        values.sort(key=lambda val: 0 if val else 1)

        i = 0
        for processor in self.processor_process_dict.keys():
            self.processor_process_dict[processor] = values[i]
            i += 1

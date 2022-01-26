import fcfs
import strategies as s


class PriorityFcfsSimple(fcfs.FCFS):
    def __init__(self, processors_num):
        super().__init__(processors_num)

    def put_new_process_on_processor(self, processor) -> s.Process:
        best_proc = None
        for proc in self.process_list:
            if (proc not in self.processor_process_dict.values()) and proc.time_left > 0:
                if not best_proc:
                    best_proc = proc
                elif proc.priority < best_proc.priority:
                    best_proc = proc
                elif proc.priority == best_proc.priority:
                    if proc.start_time < best_proc.start_time:
                        best_proc = proc
        
        self.processor_process_dict[processor] = best_proc
        return self.processor_process_dict[processor]

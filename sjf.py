import strategy as s


class SJF(s.SimpleStrategy):
    def plan_time_quantum(self) -> s.Schedule_state:
        return super()._plan_time_quantum(self._chose_process_to_put_on_processor)

    def _chose_process_to_put_on_processor(self) -> s.Process:
        best_proc = None
        for proc in self.process_list:
            if (proc not in self.processor_process_dict.values()) and proc.time_left > 0:
                if not best_proc:
                    best_proc = proc
                elif proc.time_left < best_proc.time_left:
                    best_proc = proc

        return best_proc

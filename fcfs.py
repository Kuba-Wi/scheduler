import strategy as s


class FCFS(s.SimpleStrategy):
    def plan_time_quantum(self) -> s.ScheduleState:
        return super()._plan_time_quantum(self._chose_process_to_put_on_processor)

    def _chose_process_to_put_on_processor(self) -> s.Process:
        best_proc = None
        for proc in self._process_list:
            if (proc not in self._processor_process_dict.values()) and proc.time_left > 0:
                if not best_proc:
                    best_proc = proc
                elif proc.start_time < best_proc.start_time:
                    best_proc = proc

        return best_proc


class PriorityFcfs(s.Strategy):
    def _chose_process_to_put_on_processor(self) -> s.Process:
        best_proc = None
        for proc in self._process_list:
            if (proc not in self._processor_process_dict.values()) and proc.time_left > 0:
                if not best_proc:
                    best_proc = proc
                elif proc.priority < best_proc.priority:
                    best_proc = proc
                elif proc.priority == best_proc.priority:
                    if proc.start_time < best_proc.start_time:
                        best_proc = proc

        return best_proc


class SimplePriorityFcfs(s.SimpleStrategy, PriorityFcfs):
    def plan_time_quantum(self) -> s.ScheduleState:
        return super()._plan_time_quantum(self._chose_process_to_put_on_processor)


class PriorityFcfsWithDispossess(s.StrategyWithDispossess, PriorityFcfs):
    def plan_time_quantum(self) -> s.ScheduleState:
        return super()._plan_time_quantum(self._chose_process_to_put_on_processor)

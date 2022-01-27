import strategy as s
import fcfs
import sjf
import srtf


def get_strategy_from_code(code):
    match code:
        case s.StrategyCode.FCFS:
            return fcfs.FCFS
        case s.StrategyCode.SJF:
            return sjf.SJF
        case s.StrategyCode.SRTF:
            return srtf.SRTF
        case s.StrategyCode.PRIORITY_FCFS:
            return fcfs.PriorityFcfsWithDispossess
        case s.StrategyCode.PRIORITY_SRTF:
            return srtf.PrioritySrtf
        case s.StrategyCode.PRIORITY_SIMPLE_FCFS:
            return fcfs.SimplePriorityFcfs
        case _:
            return None

def main():
    line = input()
    input_list = line.split()
    strategy_code = int(input_list[0])
    if len(input_list) == 2:
        processors_num = int(input_list[1])
    else:
        processors_num = 1

    strategy = get_strategy_from_code(strategy_code)
    scheduler = strategy(int(processors_num))
    while scheduler.read_line():
        scheduler.plan_time_quantum()
        scheduler.print_processor_state()

    while scheduler.plan_time_quantum() == s.ScheduleState.ONGOING:
        scheduler.print_processor_state()

    scheduler.print_processor_state()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import fcfs
import roundRobin as rr
import sjf
import srtf
import strategy as s


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
        case s.StrategyCode.ROUND_ROBIN:
            return rr.RoundRobin
        case _:
            return None


def main():
    try:
        line = input()
        input_list = line.split()
        strategy_code = int(input_list[0])

        if len(input_list) >= 2:
            processors_num = int(input_list[1])
        else:
            processors_num = 1

        if len(input_list) == 3:
            time_quantum = int(input_list[2])
        else:
            time_quantum = 1
    except:
        print("Wrong input, exit")
        exit()

    strategy = get_strategy_from_code(strategy_code)
    if not strategy:
        print("Wrong strategy option")
        exit()

    if strategy == rr.RoundRobin:
        scheduler = strategy(processors_num, time_quantum)
    else:
        scheduler = strategy(processors_num)

    while scheduler.read_line():
        scheduler.plan_time_quantum()
        scheduler.print_processor_state()

    while scheduler.plan_time_quantum() == s.ScheduleState.ONGOING:
        scheduler.print_processor_state()

    scheduler.print_processor_state()


if __name__ == '__main__':
    main()

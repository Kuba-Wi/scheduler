import strategy as s
import fcfs
import sjf


def main():
    processors_num = input()
    scheduler = fcfs.FCFS(int(processors_num))
    while scheduler.read_line():
        scheduler.plan_time_quantum()
        scheduler.print_processor_state()

    while scheduler.plan_time_quantum() == s.Schedule_state.ONGOING:
        scheduler.print_processor_state()

    scheduler.print_processor_state()


if __name__ == '__main__':
    main()

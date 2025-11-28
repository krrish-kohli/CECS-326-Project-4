# CECS-326 – Group Project 4: CPU Scheduling Algorithms

This project implements three classic CPU scheduling algorithms in Python:
First-Come First-Served (FCFS), Priority Scheduling, and Round-Robin (RR).
The simulator reads a list of tasks (name, priority, CPU burst), schedules them according to the selected algorithm, and prints the execution order and timing information.

All tasks are assumed to arrive at time 0, and the simulation is non-preemptive, except for Round-Robin where time quantum = 10 ms.

Requirements

OS: Linux, macOS, or Windows

Python: Version 3.8 or newer

No external libraries required

How to Run

Each scheduling algorithm is implemented in a separate file.
The main program that loads tasks and runs the chosen scheduler is:

driver.py

Running FCFS
python3 driver.py fcfs schedule.txt

Running Priority Scheduling
python3 driver.py priority schedule.txt

Running Round-Robin Scheduling
python3 driver.py rr schedule.txt

Input Format

schedule.txt must contain tasks in this format:

T1, 4, 20
T2, 2, 25
T3, 3, 25
T4, 3, 15
T5, 10, 10


Format:
[TaskName], [Priority], [CPU Burst]

Example Output (FCFS Example)
============================================================
                FCFS SCHEDULING SIMULATION
============================================================

Loaded Tasks:
T1 (priority=4, burst=20)
T2 (priority=2, burst=25)
T3 (priority=3, burst=25)
T4 (priority=3, burst=15)
T5 (priority=10, burst=10)

============================================================
EXECUTION ORDER
============================================================

Running T1 for 20 ms
Running T2 for 25 ms
Running T3 for 25 ms
Running T4 for 15 ms
Running T5 for 10 ms

============================================================
SUMMARY
============================================================
Total CPU time: 95 ms
Average waiting time: 41.0 ms
Average turnaround time: 60.0 ms

Example Output (Priority Scheduling Example)
============================================================
           PRIORITY SCHEDULING SIMULATION
============================================================

Execution Order (highest priority first):
T5 (priority=10)
T1 (priority=4)
T3 (priority=3)
T4 (priority=3)
T2 (priority=2)

...

Example Output (Round-Robin Example)

Time quantum = 10 ms

============================================================
            ROUND ROBIN (Q = 10 ms)
============================================================

Running T1 for 10 ms
Running T2 for 10 ms
Running T3 for 10 ms
Running T4 for 10 ms
Running T5 for 10 ms
Running T1 for 10 ms
Running T2 for 10 ms
...
============================================================
Simulation complete.

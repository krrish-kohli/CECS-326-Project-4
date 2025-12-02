# CECS-326 – Group Project 4: CPU Scheduling Algorithms

The project implements three classic CPU scheduling algorithms:

- **FCFS (First-Come, First-Served)**
- **Priority Scheduling**
- **Round-Robin (RR)** with a fixed **time quantum of 10 ms**

You provide a schedule file as input; the driver will load tasks and run **all three algorithms sequentially** (FCFS → Priority → RR). Output includes the execution trace and total execution time for each algorithm.

---

## Requirements

- A system with Python installed  
- A terminal/command prompt to run the program

- Python 3.x (no external libraries required)

---

## How to Run

The program reads a schedule file and then runs **all three** algorithms in order:
FCFS → Priority → Round-Robin (time quantum = 10ms). You do **not** pass an algorithm name on the command line.

Run it like this (Python 3 recommended):

```bash
python3 driver.py Schedule.txt
```

On Windows, python may map to Python 3:

```bash
python driver.py Schedule.txt
````

## Running FCFS

This runs automatically when you execute `driver.py` (the driver sequentially runs FCFS, Priority, and RR). If you only want to see this algorithm, temporarily comment out the other `schedule_*` calls in `driver.py`.

## Running Priority Scheduling

This runs automatically when you execute `driver.py` (the driver sequentially runs FCFS, Priority, and RR). If you only want to see this algorithm, temporarily comment out the other `schedule_*` calls in `driver.py`.

## Running Round-Robin Scheduling

This runs automatically when you execute `driver.py` (the driver sequentially runs FCFS, Priority, and RR). If you only want to see this algorithm, temporarily comment out the other `schedule_*` calls in `driver.py`.

## Input Format

`Schedule.txt` must contain one task per line in the format:

`TaskName, Priority, CPU_Burst`

- Commas are required; whitespace is ignored around fields.
- Blank lines are allowed.
- Lines starting with # are treated as comments and ignored.

Example (`Schedule.txt`):
```bash
T1, 4, 20
T2, 2, 25
T3, 3, 25
T4, 3, 15
T5, 10, 10
```

## Example Output (FCFS Example)

```bash
============================================================
FCFS (First-Come, First-Served) Scheduling
============================================================
Running task = [T1] priority = [4] burst = [20]
Running task = [T2] priority = [2] burst = [25]
Running task = [T3] priority = [3] burst = [25]
Running task = [T4] priority = [3] burst = [15]
Running task = [T5] priority = [10] burst = [10]

Total execution time: 95 ms
============================================================
```

## Example Output (Priority Scheduling Example)

```bash
============================================================
Priority Scheduling
============================================================
Running task = [T1] priority = [4] burst = [20]
Running task = [T3] priority = [3] burst = [25]
Running task = [T4] priority = [3] burst = [15]
Running task = [T2] priority = [2] burst = [25]
Running task = [T5] priority = [10] burst = [10]

Total execution time: 95 ms
============================================================
```

## Example Output (Round-Robin Example)

```bash
============================================================
Round-Robin (RR) Scheduling (Time Quantum = 10ms)
============================================================
Running task = [T1] priority = [4] burst = [10]
Running task = [T2] priority = [2] burst = [10]
Running task = [T3] priority = [3] burst = [10]
Running task = [T4] priority = [3] burst = [10]
Running task = [T5] priority = [10] burst = [10]
Running task = [T1] priority = [4] burst = [10]
Running task = [T2] priority = [2] burst = [10]
Running task = [T3] priority = [3] burst = [10]
Running task = [T4] priority = [3] burst = [5]
Running task = [T2] priority = [2] burst = [5]
Running task = [T3] priority = [3] burst = [5]

Total execution time: 95 ms
============================================================
```

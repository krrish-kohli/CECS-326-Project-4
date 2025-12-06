# CECS-326 – Group Project 4: CPU Scheduling Algorithms

The project implements three classic CPU scheduling algorithms:

- **FCFS (First-Come, First-Served)**
- **Priority Scheduling**
- **Round-Robin (RR)** with a fixed **time quantum of 10 ms**

In this implementation, each scheduling algorithm is in its own Python module, and a separate **test driver** runs a small built-in set of tasks through all three algorithms.  
You also provide a `schedule.txt` file in the same directory; the driver **checks that this file exists and is non-empty**, but in the current version it does **not yet parse that file into tasks**. Instead, it uses an internal list of three sample tasks to produce an execution trace and total execution time for each algorithm.

---

## Requirements

- A system with Python installed  
- A terminal/command prompt to run the program
- Python 3.x (no external libraries required)

---

## How to Run

From the directory containing the files, run:

```python
python3 driver.py
# or, equivalently:
python3 driver.py schedule.txt
```
```python
python driver.py
# or, equivalently:
python driver.py schedule.txt
```

## Example Output (FCFS Example)

```text
Reading schedule from: schedule.txt

============================================================
Loaded Tasks:
============================================================
Task: T1, Priority: 4, Burst: 20ms
Task: T2, Priority: 2, Burst: 25ms
Task: T3, Priority: 3, Burst: 25ms
Task: T4, Priority: 3, Burst: 15ms
Task: T5, Priority: 10, Burst: 10ms
============================================================


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


============================================================
Priority Scheduling
============================================================

Running task = [T5] priority = [10] burst = [10]
Running task = [T1] priority = [4] burst = [20]
Running task = [T3] priority = [3] burst = [25]
Running task = [T4] priority = [3] burst = [15]
Running task = [T2] priority = [2] burst = [25]

Total execution time: 95 ms
============================================================


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


All scheduling algorithms completed.
```

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

```bash
python3 driver.py
# or, equivalently:
python3 driver.py Schedule.txt
```
```bash
python driver.py
# or, equivalently:
python driver.py Schedule.txt
```

## Example Output (FCFS Example)

```bash
============================================================
CPU Scheduler Test Suite
============================================================

Testing imports...
✓ task.py imported successfully
✓ schedule_fcfs.py imported successfully
✓ schedule_priority.py imported successfully
✓ schedule_rr.py imported successfully

Testing schedule file...
✓ schedule.txt found with 5 tasks

Running quick functionality test...

--- Testing FCFS ---

============================================================
FCFS (First-Come, First-Served) Scheduling
============================================================

Running task = [T1] priority = [3] burst = [10]
Running task = [T2] priority = [5] burst = [15]
Running task = [T3] priority = [2] burst = [20]

Total execution time: 45 ms
============================================================


--- Testing Priority ---

============================================================
Priority Scheduling
============================================================

Running task = [T2] priority = [5] burst = [15]
Running task = [T1] priority = [3] burst = [10]
Running task = [T3] priority = [2] burst = [20]

Total execution time: 45 ms
============================================================


--- Testing Round-Robin ---

============================================================
Round-Robin (RR) Scheduling (Time Quantum = 10ms)
============================================================

Running task = [T1] priority = [3] burst = [10]
Running task = [T2] priority = [5] burst = [10]
Running task = [T3] priority = [2] burst = [10]
Running task = [T2] priority = [5] burst = [5]
Running task = [T3] priority = [2] burst = [10]

Total execution time: 45 ms
============================================================


✓ All schedulers executed successfully!

============================================================
✓ ALL TESTS PASSED!
Your code is ready to submit!
============================================================
```

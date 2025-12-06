# CECS 326 — Group Project 4 Report
- **Project Title:** CPU Scheduling (FCFS, Priority, Round-Robin)
- **Group Members:**
  - Krrish Kohli, 031530055
  - Beau Cordero, 029378347

---

## 1. Objective

Implement three classic CPU scheduling policies and demonstrate their behavior:

- **FCFS (First-Come, First-Served)** — non-preemptive, runs tasks in the order given  
- **Priority Scheduling** — non-preemptive, always chooses the remaining task with the highest priority value  
- **Round-Robin (RR)** — preemptive, with **time quantum = 10 ms**

In our Python implementation:
- Each scheduling algorithm is implemented in its own module:
  - `schedule_fcfs.py`
  - `schedule_priority.py`
  - `schedule_rr.py`
- A shared `Task` abstraction and `run()` helper are defined in `task.py`.
- A separate driver, `driver.py`, acts as a **CPU Scheduler Test Suite**:
  - It tests that required modules can be imported.
  - It checks that a file named `schedule.txt` exists and is non-empty.
  - It constructs a **built-in test workload of three tasks** and runs all three schedulers on that workload.
- The file `schedule.txt` contains a 5-task example schedule (matching the project description), but in the current version of the program it is used **only for a sanity check (existence and line count)** and is **not yet parsed into tasks by `driver.py`**.

The goal is to verify that the schedulers themselves behave correctly given a list of `Task` objects and to provide a structured test harness around them.

---

## 2. Design of the Program

### a) Program structure
The project is organized into a driver and one module per scheduling policy:

- `driver.py`  
  - Entry point and **test harness**.  
  - Does **not** parse `Schedule.txt`.  
  - Checks that `schedule.txt` is present and non-empty.  
  - Builds an internal list of three test tasks and runs FCFS, Priority, and RR on that list.
- `task.py`  
  - Defines the `Task` class and the `run(task, burst_time)` helper, which prints a standardized “Running task = [...]” line that all schedulers use.
- `schedule_fcfs.py`  
  - FCFS implementation (non-preemptive).
- `schedule_priority.py`  
  - Priority implementation (non-preemptive).
- `schedule_rr.py`  
  - Round-Robin implementation with **quantum = 10 ms**.
- `Schedule.txt`  
  - Example input file containing 5 tasks in the format `TaskName, Priority, Burst`.  
  - Currently used only for the driver’s sanity check that a schedule file exists and has at least one task line.

**Execution flow (high level):**
1. `driver.py` runs `test_imports()` to verify that `task.py` and all scheduler modules can be imported.  
2. `driver.py` runs `test_schedule_file()` to ensure a `schedule.txt` file exists and is non-empty.  
3. If both tests pass, `driver.py` calls `run_quick_test()`, which:
   - Creates a built-in list of three `Task` objects:
     - T1: priority 3, burst 10 ms  
     - T2: priority 5, burst 15 ms  
     - T3: priority 2, burst 20 ms  
   - Calls `schedule_fcfs.schedule(...)`, `schedule_priority.schedule(...)`, and `schedule_rr.schedule(...)` on copies of that list.
4. Each scheduler prints an execution trace using the shared `run()` helper and prints its total execution time at the end.
5. The driver prints a final summary (“✓ ALL TESTS PASSED!” or “✗ SOME TESTS FAILED”).

### b) State representation
- **Task (`task.py`):**
  ```python
  class Task:
      def __init__(self, name , priority, burst):
          self.name = name
          self.priority = priority
          self.burst = burst
          self.remaining_burst = burst

      def __str__(self):
          return f"Task: {self.name}, Priority: {self.priority}, Burst: {self.burst}ms"
      def __repr__(self):
          return self.__str__()

  def run(Task, burst_time):
      print(f"Running task = [{Task.name}] priority = [{Task.priority}] burst = [{burst_time}]")
  ```
- name: String identifier (e.g., "T1").
- priority: Integer priority (larger value = higher priority in our implementation).
- burst: Original CPU burst in milliseconds.
- remaining_burst: Used by Round-Robin to track how much CPU time the task still needs.
- run(task, burst_time): Prints the execution of a burst of length burst_time for that task. All scheduling policies call this function instead of printing directly, so the output format is consistent.
- We do not store arrival times; all tasks are assumed to be available at time 0 in this version.

### c) Scheduling policies

All three scheduling policies operate on an in-memory list of `Task` objects and use the shared `run()` helper.

1. **FCFS (First-Come, First-Served)** — `schedule_fcfs.py`  
   - Keeps a working copy of the task list.  
   - Repeatedly takes the **first** task from the list (index 0).  
   - Calls `run(current, current.burst)` to execute it to completion.  
   - Adds `current.burst` to `total_time` and removes the task from the list.  
   - When the list is empty, prints `Total execution time: ...`.

2. **Priority Scheduling** — `schedule_priority.py`  
   - Keeps a working copy of the task list.  
   - On each step, scans the list for the task with **maximum** `priority`.  
   - If there are ties, the first task with that maximum priority is chosen.  
   - Calls `run(current, current.burst)` to execute it to completion.  
   - Adds `current.burst` to `total_time` and removes the task.  
   - When the list is empty, prints the total execution time.

3. **Round-Robin (RR)** — `schedule_rr.py`  
   - Uses a constant `TIME_QUANTUM = 10`.  
   - Builds a queue of cloned `Task` objects (so the original list is not mutated).  
   - While the queue is not empty:
     - Takes the task at the **front**.  
     - Calculates `time_to_run = min(TIME_QUANTUM, current.remaining_burst)`.  
     - Calls `run(current, time_to_run)`.  
     - Decrements `current.remaining_burst` by `time_to_run`.  
     - Adds `time_to_run` to `total_time`.  
     - Removes the task from the front of the queue.  
     - If `current.remaining_burst > 0`, appends the task to the **back** of the queue.  
   - Prints the total execution time when all tasks finish.

### d) Round-Robin quantum behavior

With **q = 10 ms**, no task can use the CPU for more than 10 ms at a time unless it has less than 10 ms remaining.

For the built-in test workload:

- T1: priority 3, burst 10  
- T2: priority 5, burst 15  
- T3: priority 2, burst 20  

Round-Robin proceeds as:

1. T1 runs for 10 ms → done (0 remaining)  
2. T2 runs for 10 ms → 5 remaining  
3. T3 runs for 10 ms → 10 remaining  
4. T2 runs for 5 ms → done  
5. T3 runs for 10 ms → done  

Total CPU time = 10 + 10 + 10 + 5 + 10 = **45 ms**.

This demonstrates that:

- The quantum is enforced correctly.  
- Tasks with remaining work are requeued.  
- Overall CPU time is still the sum of burst times, since context-switch cost is not modeled.

### e) Example input file

`Schedule.txt` contains the 5-task example from the project description:

```text
T1, 4, 20
T2, 2, 25
T3, 3, 25
T4, 3, 15
T5, 10, 10
```

Interpretation:

- Column 1: Task name (e.g., `T1`).  
- Column 2: Priority (1–10, where we treat a higher number as higher priority).  
- Column 3: CPU burst time in milliseconds.

In the **current implementation**:

- `driver.py` only checks that a file named `schedule.txt` exists and contains at least one non-empty line.  
- It does **not** parse this file into tasks yet, so the 5-task schedule is not used in the scheduler run.  
- All schedulers in the test harness operate on the built-in 3-task workload defined inside `run_quick_test()`.

### f) Example outputs

A sample full run of `driver.py` (with all files present and `schedule.txt` containing 5 lines) looks like this:

```text
python3 driver.py schedule.txt

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

Key points:

- FCFS runs tasks in list order: T1 → T2 → T3.  
- Priority runs them by descending priority: T2 → T1 → T3.  
- Round-Robin time-slices them with `q = 10 ms`, giving multiple slices to T2 and T3.  
- All three report a total execution time of 45 ms, which matches the sum of their bursts.

### g) Discussion of behavior

- **FCFS:**
  - Simple and predictable.  
  - Preserves the order of the input list.  
  - For workloads where an early task has a long burst, later tasks may wait a long time (convoy effect).

- **Priority Scheduling:**
  - Ensures that high-priority tasks are completed first.  
  - May cause starvation for low-priority tasks if there are always higher-priority tasks in the queue.  
  - Our implementation is non-preemptive (no re-evaluation during a task’s execution).

- **Round-Robin:**
  - Preemptive and better suited for time-sharing or interactive systems.  
  - Every task gets a fair turn every `TIME_QUANTUM` units of time.  
  - Total CPU time is unchanged but response time improves, especially for shorter tasks.  
  - In this project, context-switch overhead is ignored, so Round-Robin is “free” apart from the splitting of bursts.

### h) Robustness and input handling

- The driver **checks for the presence and non-emptiness** of `schedule.txt`.  
- If the file is missing or empty, `test_schedule_file()` fails and the test suite reports that some tests failed.  
- Input parsing from `schedule.txt` (e.g., skipping comments, trimming whitespace, validating fields) is **not implemented yet**. All actual test runs use the built-in 3-task workload.

### i) Testing & edge cases

Within the current design, the main edge cases handled are:

- **Missing modules:**  
  - If `task.py` or any scheduling module cannot be imported, `test_imports()` prints an error and stops the test run.

- **Missing or empty schedule file:**  
  - If `schedule.txt` does not exist or has no non-empty lines, `test_schedule_file()` fails and the quick functionality test is skipped.

- **Scheduler correctness on the built-in workload:**  
  - Verifies that:
    - FCFS preserves list order.  
    - Priority always chooses the highest-priority remaining task.  
    - RR rotates tasks and decrements `remaining_burst` correctly with `q = 10 ms`.  
  - Confirms that the total execution time equals the sum of the bursts (45 ms) for all three algorithms.

---

## 3. How to Run
From the directory containing the files, run:
```python
python3 driver.py
# or, equivalently:
python3 driver.py schedule.txt
```
or on some systems:
```python
python driver.py
# or, equivalently:
python driver.py schedule.txt
```


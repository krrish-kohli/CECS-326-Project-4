# CECS 326 — Group Project 4 Report
- **Project Title:** CPU Scheduling (FCFS, Priority, Round-Robin)
- **Group Members:**
  - Krrish Kohli, 031530055
  - Beau Cordero, 029378347

---

## 1. Objective

Implement a CPU scheduling simulator that runs three classic policies over a common task set:

- **FCFS (First-Come, First-Served)** — non-preemptive, in arrival/file order  
- **Priority Scheduling** — non-preemptive, chooses highest-priority task (per integer priority rule)  
- **Round-Robin (RR)** — preemptive, **time quantum = 10 ms**

The simulator reads tasks from an input file and executes **all three algorithms sequentially** (FCFS → Priority → RR), printing the execution trace and the total CPU time for each algorithm.

---

## 2. Design of the Program

### a) Program structure
The project is organized into a driver and one module per scheduling policy:

- `driver.py` — Entry point. Loads tasks from `Schedule.txt`, then runs FCFS, Priority, and RR in that order. Handles parsing, validation, and per-algorithm printing delimiters.
- `task.py` — Defines `Task(name, priority, burst, remaining_burst)` and a `run(task, burst_time)` helper that prints the current execution slice.
- `schedule_fcfs.py` — FCFS implementation (non-preemptive).
- `schedule_priority.py` — Priority implementation (non-preemptive).
- `schedule_rr.py` — RR implementation with **quantum = 10 ms**.
- `Schedule.txt` — Example input file.

**Execution flow (high level):**
1. Parse `Schedule.txt` → in-memory list of `Task` objects  
2. Run FCFS → print trace & total  
3. Run Priority → print trace & total  
4. Run RR (quantum slicing) → print trace & total

### b) State representation
- **Task:**  
  - `name: str` (e.g., `"T1"`)  
  - `priority: int` (lower/higher numeric priority depending on spec; code consistently uses the provided integer to compare)  
  - `burst: int` (CPU burst in ms)  
  - `remaining_burst: int` (initialized to `burst`)
- **Ready list / queue:**  
  - For **FCFS**: simple list in file order  
  - For **Priority**: list scanned for the “highest-priority” task  
  - For **RR**: FIFO queue rotated after each quantum; tasks with remaining time re-enqueued
- **Input format (`Schedule.txt`):**
  ```TaskName, Priority, CPU_Burst```
  - Commas are required; surrounding whitespace is ignored  
  - Blank lines are allowed  
  - Lines beginning with `#` are comments and ignored
- **Example:**
  
  ```bash
    T1, 4, 20
    T2, 2, 25
    T3, 3, 25
    T4, 3, 15
    T5, 10, 10
  ```


### c) FCFS scheduler (`schedule_fcfs.schedule(task_list)`)
- **Policy:** Non-preemptive, execute tasks in the order they appear (file order)  
- **Mechanics:** For each task, call `run(task, task.burst)` once and accumulate total time  
- **Output:**  
  - Header block (with separator lines)  
  - One “Running task …” line per task  
  - `Total execution time: <sum of bursts> ms`

### d) Priority scheduler (`schedule_priority.schedule(task_list)`)
- **Policy:** Non-preemptive, repeatedly pick the **highest-priority** task among remaining tasks  
- **Mechanics:**  
  - Scan remaining tasks to select the best candidate  
  - `run(task, task.burst)` once; remove from remaining; accumulate total  
- **Notes:** Without aging, low-priority tasks may starve in some workloads  
- **Output:** Same header/trace/total style as FCFS

### e) Round-Robin scheduler (`schedule_rr.schedule(task_list)`)
- **Policy:** Preemptive, **quantum = 10 ms**  
- **Mechanics:**  
  - Initialize FIFO ready queue with all tasks  
  - Pop front → slice `min(remaining_burst, 10)` via `run(task, slice)`  
  - If `remaining_burst > 0`, re-enqueue; otherwise complete  
  - Continue until queue empty; accumulate total (sum of full bursts)
- **Behavior:** Better interactivity/fairness vs. FCFS; quantum trades responsiveness vs. overhead (context switch cost not explicitly modeled)

### f) Output and execution
- If args are wrong:
  ```
  Usage: python driver.py <schedule_file>
  Example: python driver.py schedule.txt
  ```
- Otherwise:
  ```
  Reading schedule from: <your-file>
  ```

**Loaded tasks block (before any scheduler runs)**
```
============================================================
Loaded Tasks:
Task: T1, Priority: 4, Burst: 20ms
Task: T2, Priority: 2, Burst: 25ms
Task: T3, Priority: 3, Burst: 25ms
Task: T4, Priority: 3, Burst: 15ms
Task: T5, Priority: 10, Burst: 10ms
============================================================
```

**Per-algorithm sections (in this order):**

1) FCFS
```
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

2) Priority
```
============================================================
Priority Scheduling
============================================================
... one "Running task = [...]" line per task (full bursts) ...
Total execution time: 95 ms
============================================================
```

3) Round-Robin (q = 10 ms)
```
============================================================
Round-Robin (RR) Scheduling (Time Quantum = 10ms)
============================================================
... one "Running task = [...]" line per quantum slice (10ms or remainder) ...
Total execution time: 95 ms
============================================================
```

**Program end**
```
All scheduling algorithms completed.
```

### g) Correctness & scheduling properties
- **FCFS:** Correctly preserves input order; demonstrates convoy effect when early tasks have long bursts  
- **Priority:** Always chooses the highest-priority remaining task; starvation is possible without aging  
- **RR:** Correctly time-slices with **q = 10 ms** and rotates tasks with remaining work; improves responsiveness and fairness

### h) Robustness and input handling
- Ignores blank lines and lines beginning with `#`  
- Trims whitespace; validates that each non-comment line contains three comma-separated fields  
- Prints consistent headers and totals for each algorithm  
- Works without third-party dependencies (Python 3.x standard library)

### i) Testing & edge cases
- **Comment/blank-line handling:** Confirmed parser behavior  
- **Tie scenarios:** Priority ties behave deterministically per implementation order/criterion  
- **Large bursts / many tasks:** Schedulers still produce correct traces and totals  
- **RR rotation:** Verified repeated slicing and re-enqueue until tasks complete

---

## 3. How to Run
- Use Python 3.x in a terminal:
  ```bash
  python3 driver.py Schedule.txt
  ```
- The driver runs FCFS → Priority → RR automatically
- On Windows, python may already map to Python 3:
  ```bash
  python driver.py Schedule.txt
  ```

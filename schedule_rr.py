from task import Task, run

# Time quantum for Round-Robin scheduling
TIME_QUANTUM = 10


def pick_next_task(task_queue):

    if not task_queue:
        return None
    return task_queue[0]


def schedule(task_list):

    print("\n" + "=" * 60)
    print("Round-Robin (RR) Scheduling (Time Quantum = 10ms)")
    print("=" * 60 + "\n")

    # Create a queue with copies of tasks (to preserve remaining burst time)
    task_queue = []
    for task in task_list:
        # Create a new task object to track remaining burst time
        new_task = Task(task.name, task.priority, task.burst)
        task_queue.append(new_task)

    total_time = 0

    while task_queue:
        # Pick the next task (first in queue)
        current_task = pick_next_task(task_queue)

        if current_task:
            # Determine how long to run this task
            # Run for time quantum or remaining burst, whichever is smaller
            burst_time = min(TIME_QUANTUM, current_task.remaining_burst)

            # Run the task
            run(current_task, burst_time)
            total_time += burst_time

            # Update remaining burst time
            current_task.remaining_burst -= burst_time

            # Remove task from front of queue
            task_queue.pop(0)

            # If task still has remaining burst time, add it to back of queue
            if current_task.remaining_burst > 0:
                task_queue.append(current_task)

    print(f"\nTotal execution time: {total_time} ms")
    print("=" * 60 + "\n")
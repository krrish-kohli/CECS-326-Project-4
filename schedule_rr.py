from task import Task, run

# Time quantum for Round-Robin
TIME_QUANTUM = 10


def pick_next_task(task_queue):
    # Return the first task in queue (FIFO)
    if not task_queue:
        return None
    return task_queue[0]


def schedule(task_list):
    # Schedule tasks using Round-Robin with time quantum = 10ms
    print("\n" + "=" * 60)
    print("Round-Robin (RR) Scheduling (Time Quantum = 10ms)")
    print("=" * 60 + "\n")

    # Create queue with task copies (to track remaining burst)
    queue = []
    for task in task_list:
        new_task = Task(task.name, task.priority, task.burst)
        queue.append(new_task)

    total_time = 0

    # Process tasks in circular order
    while queue:
        # Get next task from queue
        current = pick_next_task(queue)

        if current:
            # Run for time quantum or remaining burst (whichever is less)
            time_to_run = min(TIME_QUANTUM, current.remaining_burst)

            # Execute the task
            run(current, time_to_run)
            total_time += time_to_run

            # Update remaining burst time
            current.remaining_burst -= time_to_run

            # Remove from front of queue
            queue.pop(0)

            # If task not finished, add to back of queue
            if current.remaining_burst > 0:
                queue.append(current)

    print(f"\nTotal execution time: {total_time} ms")
    print("=" * 60 + "\n")
from task import run


def pick_next_task(task_list):
    # Return the first task in the list (FCFS order)
    if not task_list:
        return None
    return task_list[0]


def schedule(task_list):
    # Schedule tasks using FCFS - execute in order of appearance
    print("\n" + "=" * 60)
    print("FCFS (First-Come, First-Served) Scheduling")
    print("=" * 60 + "\n")

    # Make a copy to avoid modifying original list
    tasks = task_list.copy()
    total_time = 0

    # Process each task in order
    while tasks:
        # Get next task
        current = pick_next_task(tasks)

        if current:
            # Run the task for its full burst time
            run(current, current.burst)
            total_time += current.burst
            # Remove from list
            tasks.remove(current)

    print(f"\nTotal execution time: {total_time} ms")
    print("=" * 60 + "\n")

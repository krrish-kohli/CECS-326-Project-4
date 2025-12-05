from task import run


def pick_next_task(task_list):
    # Find and return the task with highest priority
    if not task_list:
        return None

    # Start with first task
    highest = task_list[0]
    # Find task with highest priority
    for task in task_list:
        if task.priority > highest.priority:
            highest = task

    return highest


def schedule(task_list):
    # Schedule tasks by priority (highest first)
    print("\n" + "=" * 60)
    print("Priority Scheduling")
    print("=" * 60 + "\n")

    # Make a copy to avoid modifying original list
    tasks = task_list.copy()
    total_time = 0

    # Process tasks in priority order
    while tasks:
        # Get highest priority task
        current = pick_next_task(tasks)

        if current:
            # Run the task for its full burst time
            run(current, current.burst)
            total_time += current.burst
            # Remove from list
            tasks.remove(current)

    print(f"\nTotal execution time: {total_time} ms")
    print("=" * 60 + "\n")
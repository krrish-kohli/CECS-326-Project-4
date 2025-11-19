from task import run


def pick_next_task(task_list):

    if not task_list:
        return None

    # Find the task with the highest priority
    highest_priority_task = task_list[0]
    for task in task_list:
        if task.priority > highest_priority_task.priority:
            highest_priority_task = task

    return highest_priority_task


def schedule(task_list):

    print("\n" + "=" * 60)
    print("Priority Scheduling")
    print("=" * 60 + "\n")

    # Create a copy of the task list to avoid modifying the original
    remaining_tasks = task_list.copy()
    total_time = 0

    while remaining_tasks:
        # Pick the task with highest priority
        current_task = pick_next_task(remaining_tasks)

        if current_task:
            # Run the task for its full burst time
            run(current_task, current_task.burst)
            total_time += current_task.burst


            remaining_tasks.remove(current_task)

    print(f"\nTotal execution time: {total_time} ms")
    print("=" * 60 + "\n")
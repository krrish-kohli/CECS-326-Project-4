from task import run

def pick_next_task(task_list):
    if not task_list:
        return None
    return task_list[0]
def schedule(task_list):
    print("\n" + "="*60)
    print("FCFS (First-Come, First-Served) Scheduling")
    print("="*60 + "\n")
    remaining_task = task_list.copy()
    total_time = 0

    while remaining_task:
        current_task = pick_next_task(remaining_tasks)
        if current_task:
            run(current_task, current_task.burst)
            total_time += current_task.burst

            remaining_tasks.remove(current_task)

    print(f"\nTotal execution time: {total_time} ms")
    print("="*60 + "\n")

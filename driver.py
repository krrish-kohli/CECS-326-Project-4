import sys
from task import Task
import schedule_fcfs
import schedule_priority
import schedule_rr


def read_schedule(filename):
    """
    Read tasks from a schedule file

    File format: task_name, priority, burst_time
    Example: T1, 4, 20

    Args:
        filename (str): Path to the schedule file

    Returns:
        list: List of Task objects
    """
    tasks = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Skip empty lines and comments
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Parse the line: task_name, priority, burst
                parts = [part.strip() for part in line.split(',')]

                if len(parts) == 3:
                    name = parts[0]
                    priority = int(parts[1])
                    burst = int(parts[2])

                    # Create and add task
                    task = Task(name, priority, burst)
                    tasks.append(task)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error parsing file: {e}")
        sys.exit(1)

    return tasks


def display_tasks(tasks):
    """
    Display the list of tasks

    Args:
        tasks (list): List of Task objects
    """
    print("\n" + "=" * 60)
    print("Loaded Tasks:")
    print("=" * 60)
    for task in tasks:
        print(task)
    print("=" * 60 + "\n")


def main():
    """
    Main function - entry point of the program
    """
    # Use schedule.txt by default, or custom file if provided
    if len(sys.argv) >= 2:
        schedule_file = sys.argv[1]
    else:
        schedule_file = "schedule.txt"  # Default file
        print("No schedule file specified, using default: schedule.txt")

    # Read the schedule file
    print(f"\nReading schedule from: {schedule_file}")
    tasks = read_schedule(schedule_file)

    if not tasks:
        print("No tasks found in schedule file.")
        sys.exit(1)

    # Display loaded tasks
    display_tasks(tasks)

    # Run FCFS scheduling
    schedule_fcfs.schedule(tasks.copy())

    # Run Priority scheduling
    schedule_priority.schedule(tasks.copy())

    # Run Round-Robin scheduling
    schedule_rr.schedule(tasks.copy())

    print("\nAll scheduling algorithms completed.\n")


if __name__ == "__main__":
    main()

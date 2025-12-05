import sys
import os


def test_imports():
    """Test if all modules can be imported"""
    print("Testing imports...")
    try:
        import task
        print("✓ task.py imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import task.py: {e}")
        return False

    try:
        import schedule_fcfs
        print("✓ schedule_fcfs.py imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import schedule_fcfs.py: {e}")
        return False

    try:
        import schedule_priority
        print("✓ schedule_priority.py imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import schedule_priority.py: {e}")
        return False

    try:
        import schedule_rr
        print("✓ schedule_rr.py imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import schedule_rr.py: {e}")
        return False

    return True


def test_schedule_file():
    """Test if schedule.txt exists and is readable"""
    print("\nTesting schedule file...")
    if not os.path.exists('schedule.txt'):
        print("✗ schedule.txt not found")
        return False

    try:
        with open('schedule.txt', 'r') as f:
            lines = f.readlines()
            if len(lines) > 0:
                print(f"✓ schedule.txt found with {len(lines)} tasks")
                return True
            else:
                print("✗ schedule.txt is empty")
                return False
    except Exception as e:
        print(f"✗ Error reading schedule.txt: {e}")
        return False


def run_quick_test():
    """Run a quick test with sample tasks"""
    print("\nRunning quick functionality test...")
    try:
        from task import Task
        import schedule_fcfs
        import schedule_priority
        import schedule_rr

        # Create test tasks
        test_tasks = [
            Task("T1", 3, 10),
            Task("T2", 5, 15),
            Task("T3", 2, 20)
        ]

        print("\n--- Testing FCFS ---")
        schedule_fcfs.schedule(test_tasks.copy())

        print("\n--- Testing Priority ---")
        schedule_priority.schedule(test_tasks.copy())

        print("\n--- Testing Round-Robin ---")
        schedule_rr.schedule(test_tasks.copy())

        print("\n✓ All schedulers executed successfully!")
        return True

    except Exception as e:
        print(f"\n✗ Error during execution: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main test function"""
    print("=" * 60)
    print("CPU Scheduler Test Suite")
    print("=" * 60 + "\n")

    all_pass = True

    # Test imports
    if not test_imports():
        all_pass = False
        print("\n⚠ Import test failed! Make sure all .py files are in the same directory.")

    # Test schedule file
    if not test_schedule_file():
        all_pass = False
        print("\n⚠ Schedule file test failed! Make sure schedule.txt exists.")

    # Run functionality test
    if all_pass:
        if not run_quick_test():
            all_pass = False

    print("\n" + "=" * 60)
    if all_pass:
        print("✓ ALL TESTS PASSED!")
        print("Your code is ready to submit!")
    else:
        print("✗ SOME TESTS FAILED")
        print("Please check the errors above and fix them.")
        print("See TROUBLESHOOTING.md for help.")
    print("=" * 60 + "\n")

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
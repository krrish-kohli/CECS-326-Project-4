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


# -------------------------------
# TASK 1: Process Creation & Input Handling
# -------------------------------

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid          # Process ID
        self.at = at            # Arrival Time
        self.bt = bt            # Burst Time
        self.ct = 0             # Completion Time
        self.tat = 0            # Turnaround Time
        self.wt = 0             # Waiting Time

# Input from user
processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    pid = i + 1
    at = int(input(f"Enter Arrival Time for P{pid}: "))
    bt = int(input(f"Enter Burst Time for P{pid}: "))
    processes.append(Process(pid, at, bt))

# -------------------------------
# TASK 2: FCFS Scheduling
# -------------------------------

def fcfs(processes):
    # Sort processes by Arrival Time
    processes.sort(key=lambda x: x.at)
    time = 0

    for p in processes:
        # Handle CPU idle condition
        if time < p.at:
            time = p.at

        # Calculate times
        p.ct = time + p.bt
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        time = p.ct

    return processes

# -------------------------------
# TASK 3: SJF Scheduling (Non-Preemptive)
# -------------------------------

def sjf(processes):
    completed = []
    time = 0

    while processes:
        # Get processes that have arrived
        available = [p for p in processes if p.at <= time]

        # If no process available, increment time
        if not available:
            time += 1
            continue

        # Select process with shortest burst time
        shortest = min(available, key=lambda x: x.bt)
        processes.remove(shortest)

        # Calculate times
        shortest.ct = time + shortest.bt
        shortest.tat = shortest.ct - shortest.at
        shortest.wt = shortest.tat - shortest.bt

        time = shortest.ct
        completed.append(shortest)

    return completed

# Function to display output
def display(processes):
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

# -------------------------------
# TASK 4: Gantt Chart (Manual in Report)
# -------------------------------
# Note: Gantt chart will be drawn in report manually

# -------------------------------
# TASK 5: Performance Analysis
# -------------------------------

def avg_times(processes):
    total_wt = sum(p.wt for p in processes)
    total_tat = sum(p.tat for p in processes)

    print("\nAverage Waiting Time:", total_wt / len(processes))
    print("Average Turnaround Time:", total_tat / len(processes))

# -------------------------------
# MAIN EXECUTION
# -------------------------------

print("\n--- FCFS ---")
fcfs_result = fcfs(processes.copy())
display(fcfs_result)
avg_times(fcfs_result)

print("\n--- SJF ---")
sjf_result = sjf(processes.copy())
display(sjf_result)
avg_times(sjf_result)
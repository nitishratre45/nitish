# CPU Scheduling Algorithms
# FCFS, SJF, Round Robin and Priority Scheduling

processes = [
    {"pid": "P1", "burst": 8, "priority": 3},
    {"pid": "P2", "burst": 4, "priority": 1},
    {"pid": "P3", "burst": 2, "priority": 4},
    {"pid": "P4", "burst": 1, "priority": 2}
]


def display_results(name, schedule, results):
    print("\\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print("Gantt Chart:")
    for pid, start, end in schedule:
        print(f"{pid} [{start}-{end}]", end=" | ")

    print("\\n\\nPID\\tBurst\\tWaiting\\tTurnaround")

    total_waiting = 0
    total_turnaround = 0

    for p in processes:
        pid = p["pid"]
        burst = p["burst"]
        waiting = results[pid]["waiting"]
        turnaround = results[pid]["turnaround"]

        print(f"{pid}\\t{burst}\\t{waiting}\\t{turnaround}")

        total_waiting += waiting
        total_turnaround += turnaround

    n = len(processes)

    print(f"\\nAverage Waiting Time = {total_waiting / n:.2f}")
    print(f"Average Turnaround Time = {total_turnaround / n:.2f}")


# FCFS Scheduling
def fcfs():
    time = 0
    schedule = []
    results = {}

    for p in processes:
        pid = p["pid"]
        burst = p["burst"]

        start = time
        time += burst

        waiting = start
        turnaround = time

        schedule.append((pid, start, time))

        results[pid] = {
            "waiting": waiting,
            "turnaround": turnaround
        }

    display_results("FCFS Scheduling", schedule, results)


# SJF Scheduling
def sjf():
    time = 0
    schedule = []
    results = {}

    ordered = sorted(processes, key=lambda p: p["burst"])

    for p in ordered:
        pid = p["pid"]
        burst = p["burst"]

        start = time
        time += burst

        waiting = start
        turnaround = time

        schedule.append((pid, start, time))

        results[pid] = {
            "waiting": waiting,
            "turnaround": turnaround
        }

    display_results("SJF Scheduling", schedule, results)


# Round Robin Scheduling
def round_robin(quantum):
    time = 0
    schedule = []

    remaining = {p["pid"]: p["burst"] for p in processes}
    completion = {}

    queue = [p["pid"] for p in processes]

    while queue:
        pid = queue.pop(0)
        start = time

        execution = min(quantum, remaining[pid])

        time += execution
        remaining[pid] -= execution

        schedule.append((pid, start, time))

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion[pid] = time

    results = {}

    for p in processes:
        pid = p["pid"]
        burst = p["burst"]

        turnaround = completion[pid]
        waiting = turnaround - burst

        results[pid] = {
            "waiting": waiting,
            "turnaround": turnaround
        }

    display_results(
        f"Round Robin Scheduling (Quantum = {quantum})",
        schedule,
        results
    )


# Priority Scheduling
def priority_scheduling():
    time = 0
    schedule = []
    results = {}

    # Lower priority number means higher priority
    ordered = sorted(processes, key=lambda p: p["priority"])

    for p in ordered:
        pid = p["pid"]
        burst = p["burst"]

        start = time
        time += burst

        waiting = start
        turnaround = time

        schedule.append((pid, start, time))

        results[pid] = {
            "waiting": waiting,
            "turnaround": turnaround
        }

    display_results("Priority Scheduling", schedule, results)


# Main Program
print("CPU SCHEDULING SIMULATION")

print("\\nProcesses:")
print("PID\\tBurst Time\\tPriority")

for p in processes:
    print(f"{p['pid']}\\t{p['burst']}\\t\\t{p['priority']}")

fcfs()
sjf()
round_robin(2)
priority_scheduling()

# PROGRAM-01: CPU Scheduling — Code Explanation

## 1. Process data
```python
processes = [
    {"pid": "P1", "burst": 8, "priority": 3},
    {"pid": "P2", "burst": 4, "priority": 1},
    {"pid": "P3", "burst": 2, "priority": 4},
    {"pid": "P4", "burst": 1, "priority": 2}
]
```
- `processes`: stores the list of processes.
- `pid`: unique process label (P1, P2, etc.).
- `burst`: CPU time required by that process.
- `priority`: priority rank. This example treats the smaller number as higher priority.
- All processes are assumed to arrive at time 0.

## 2. Display function
```python
def display_results(name, schedule, results):
```
Defines a reusable function to display the algorithm name, Gantt chart, process table, and averages. `name` is the heading; `schedule` stores execution intervals; `results` stores timing values.

- `print("\\n" + "=" * 50)`: prints a new line and 50 equals signs as a separator.
- `print(name)`: prints the current algorithm name.
- `print("Gantt Chart:")`: introduces the timeline.
- `for pid, start, end in schedule`: reads each interval tuple and unpacks its process ID, start, and end.
- `print(f"{pid} [{start}-{end}]", end=" | ")`: formats values into one line; `end` prevents a newline and adds a divider.
- The header print with `\\n` and `\\t` makes line breaks and tab-separated column names.
- `total_waiting = 0` and `total_turnaround = 0`: initialize accumulators.
- `for p in processes`: visits each process to print its metrics.
- `pid = p["pid"]`, `burst = p["burst"]`: reads fields from the current dictionary.
- `results[pid]["waiting"]` and `results[pid]["turnaround"]`: retrieves the calculated metrics for that process.
- The formatted `print` line outputs a row in the table.
- `total_waiting += waiting` and `total_turnaround += turnaround`: add current values to the totals; `+=` means add and assign.
- `n = len(processes)`: counts processes.
- The final average print statements divide each total by `n`; `:.2f` formats the value to two decimal places.

## 3. FCFS
- `def fcfs():`: defines First Come First Serve scheduling.
- `time = 0`: CPU timeline begins at zero.
- `schedule = []`: creates a list for Gantt chart intervals.
- `results = {}`: creates a dictionary to store process timing metrics.
- `for p in processes`: processes jobs in the list's original order.
- `pid` and `burst` assignments extract the current process ID and burst.
- `start = time`: records the process start time.
- `time += burst`: advances the timeline by the process's full CPU burst.
- `waiting = start`: because arrival time is zero, waiting time equals start time.
- `turnaround = time`: because arrival time is zero, turnaround equals completion time.
- `schedule.append((pid, start, time))`: records the process interval for the chart.
- The `results[pid]` dictionary saves waiting and turnaround metrics.
- `display_results(...)`: prints the FCFS report.

## 4. SJF
- `def sjf():`: defines Shortest Job First.
- The initial `time`, `schedule`, and `results` variables have the same purposes as FCFS.
- `ordered = sorted(processes, key=lambda p: p["burst"])`: makes a sorted copy ordered by burst time, shortest first. `lambda` is a small anonymous function that returns a process's burst.
- `for p in ordered`: schedules the sorted processes.
- ID/burst extraction, time advancement, waiting/turnaround calculation, schedule append, and result storage work like FCFS but use the SJF order.
- `display_results("SJF Scheduling", ...)`: displays the SJF report.

## 5. Round Robin
- `def round_robin(quantum):`: defines Round Robin; `quantum` is the maximum CPU time per turn.
- `time = 0` starts the CPU clock.
- `schedule = []` records every time slice (a process may appear multiple times).
- `remaining = {p["pid"]: p["burst"] for p in processes}`: dictionary comprehension initializes remaining CPU time for each process.
- `completion = {}`: will hold each finished process's completion time.
- `queue = [p["pid"] for p in processes]`: builds the ready queue in initial order.
- `while queue`: repeats until no unfinished process remains in the queue.
- `pid = queue.pop(0)`: removes the first queue item.
- `start = time`: records the beginning of this time slice.
- `execution = min(quantum, remaining[pid])`: chooses the smaller of the time quantum and remaining CPU time, so a process never runs beyond completion.
- `time += execution`: advances the CPU clock.
- `remaining[pid] -= execution`: subtracts time used from remaining burst.
- `schedule.append((pid, start, time))`: records this time slice.
- If remaining time is positive, `queue.append(pid)` puts the process at the queue's end so others get a turn.
- Otherwise the `else` branch records `completion[pid] = time`.
- `results = {}`: prepares the final metric dictionary.
- The process loop reads each process ID and original burst.
- `turnaround = completion[pid]`: completion time equals turnaround because arrivals are zero.
- `waiting = turnaround - burst`: total waiting is turnaround minus the CPU time spent running.
- The results dictionary stores those values.
- The multi-line `display_results(...)` call prints the Round Robin chart and statistics.

## 6. Priority Scheduling
- `def priority_scheduling():`: defines priority-based scheduling.
- `time = 0`, `schedule = []`, and `results = {}`: initialize clock, chart, and metrics.
- `ordered = sorted(processes, key=lambda p: p["priority"])`: sorts by priority number ascending (lower number is treated as higher priority).
- `for p in ordered`: runs processes in priority order.
- ID/burst extraction obtains the current job details.
- `start = time` records start time; `time += burst` completes its full burst.
- Waiting time equals start time, and turnaround equals completion time, given arrival time zero.
- `schedule.append(...)` records the execution interval.
- The result dictionary stores timing values.
- `display_results("Priority Scheduling", ...)` prints the priority report.

## 7. Main program
- `print("CPU SCHEDULING SIMULATION")`: displays the program title.
- The next two print statements introduce and label the process input table.
- `for p in processes`: iterates over each process.
- The f-string print shows its ID, burst time, and priority.
- `fcfs()`, `sjf()`, `round_robin(2)`, and `priority_scheduling()`: call the four algorithms in order. Round Robin is given quantum 2.

## 8. Formulas
- Waiting Time (WT) = Turnaround Time (TAT) − Burst Time (BT)
- Turnaround Time = Completion Time − Arrival Time
- Average WT = Sum of WT ÷ Number of processes
- Average TAT = Sum of TAT ÷ Number of processes

## 9. Viva questions
1. What is CPU scheduling?
2. What is FCFS and its main drawback?
3. What is the convoy effect?
4. Explain SJF.
5. What is a time quantum?
6. How does Round Robin work?
7. What is Priority Scheduling?
8. Define waiting time and turnaround time.
9. What is a Gantt chart?

## 10. Assumptions
- Every process arrives at time 0.
- FCFS, SJF, and Priority are non-preemptive here.
- SJF uses burst time only.
- Smaller priority number means higher priority.
- Round Robin uses quantum 2.

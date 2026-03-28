# -------------------------------
# TASK 1: System Input & Data Representation
# -------------------------------

n = int(input("Enter number of processes: "))
r = int(input("Enter number of resources: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input().split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
maximum = []
for i in range(n):
    row = list(map(int, input().split()))
    maximum.append(row)

print("\nEnter Available Resources:")
available = list(map(int, input().split()))

# -------------------------------
# TASK 2: Need Matrix Calculation
# -------------------------------

need = []
for i in range(n):
    row = []
    for j in range(r):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

print("\nNeed Matrix:")
for row in need:
    print(row)

# -------------------------------
# TASK 3: Banker’s Safety Algorithm
# -------------------------------

work = available.copy()
finish = [False] * n
safe_sequence = []

while len(safe_sequence) < n:
    found = False
    for i in range(n):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(r)):
                # Allocate resources
                for j in range(r):
                    work[j] += allocation[i][j]

                safe_sequence.append(i)
                finish[i] = True
                found = True

    if not found:
        break

# -------------------------------
# TASK 4: Safe Sequence
# -------------------------------

if len(safe_sequence) == n:
    print("\nSystem is in SAFE state")
    print("Safe sequence:", ["P" + str(i) for i in safe_sequence])
else:
    print("\nSystem is NOT in safe state")

# -------------------------------
# TASK 5: Result Analysis
# -------------------------------

if len(safe_sequence) == n:
    print("\nAnalysis: No deadlock, system is safe.")
else:
    print("\nAnalysis: Deadlock may occur, system is unsafe.")
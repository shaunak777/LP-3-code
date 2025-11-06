# Job Sequencing with Deadlines using Greedy Method

# Function to schedule jobs for maximum profit
def job_sequencing(jobs):
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    result = [False] * n   # To track free time slots
    job_order = ['-'] * n  # To store job sequence

    # For each job, find a slot before its deadline
    for i in range(n):
        for j in range(min(n, jobs[i][1]) - 1, -1, -1):
            if not result[j]:
                result[j] = True
                job_order[j] = jobs[i][0]
                break

    print("Job sequence for maximum profit:")
    print(" → ".join([job for job in job_order if job != '-']))

# --- Input Section ---
n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    name = input(f"Enter Job name {i+1}: ")
    deadline = int(input(f"Enter deadline for {name}: "))
    profit = int(input(f"Enter profit for {name}: "))
    jobs.append((name, deadline, profit))

# --- Output Section ---
job_sequencing(jobs)

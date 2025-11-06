# 0-1 Knapsack Problem using Dynamic Programming

def knapsack(W, wt, val, n):
    # Create a 2D DP table of size (n+1) x (W+1)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# ---- Input Section ----
n = int(input("Enter number of items: "))
val = []
wt = []


for i in range(n):
    val.append(int(input(f"Enter value of item {i + 1}: ")))
    wt.append(int(input(f"Enter weight of item {i + 1}: ")))

W = int(input("Enter maximum capacity of knapsack: "))

# ---- Function Call ----
max_value = knapsack(W, wt, val, n)

# ---- Output Section ----
print("Maximum value that can be put in knapsack =", max_value)

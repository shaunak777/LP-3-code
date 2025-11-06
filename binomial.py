# Program to generate Binomial Coefficients using Dynamic Programming

def binomial_coeff(n, k):
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate binomial coefficients using DP
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]

# --- Input Section ---
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

# --- Output Section ---
print(f"Binomial Coefficient C({n},{k}) =", binomial_coeff(n, k))

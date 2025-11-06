# Fractional Knapsack Problem using Greedy Method

n = int(input("Enter number of items: "))
items = []

for i in range(n):
    value = float(input(f"Enter value of item {i+1}: "))
    weight = float(input(f"Enter weight of item {i+1}: "))
    ratio = value / weight
    items.append((value, weight, ratio))

capacity = float(input("Enter knapsack capacity: "))

# Sort items by value/weight ratio (descending order)
items.sort(key=lambda x: x[2], reverse=True)

total_value = 0.0
remaining_capacity = capacity

for value, weight, ratio in items:
    if remaining_capacity >= weight:
        # Take the whole item
        total_value += value
        remaining_capacity -= weight
    else:
        # Take fraction of the item
        total_value += ratio * remaining_capacity
        break

print("\nMaximum value in Knapsack =", round(total_value, 2))

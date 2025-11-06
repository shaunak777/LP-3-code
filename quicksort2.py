import random

def deterministic_quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1]if x<=pivot]
    right=[x for x in arr[:-1]if x>pivot]
    return deterministic_quick_sort(left)+[pivot]+deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=random.choice(arr)
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if pivot==x]
    right=[x for x in arr if x>pivot]
    return randomized_quick_sort(left)+middle+randomized_quick_sort(right)

n=int(input("Enter number of Elements:"))
arr=[int(input(f"Enter element {i+1}:")) for i in range(n)]

print("\nOriginal Array:",arr)
print("Sorted (Deterministic QuickSort):",deterministic_quick_sort(arr))
print("Sorted (Randomized QuickSort):",randomized_quick_sort(arr))
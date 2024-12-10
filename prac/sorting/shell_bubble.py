# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Print the array at the beginning of this iteration
        print(f"Iteration {i + 1}: {arr}")
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # Print the array after each full pass
        print(f"After pass {i + 1}: {arr}")
    return arr

# Function to perform Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Start with a large gap, then reduce the gap
    iteration = 1
    
    while gap > 0:
        print(f"Gap {gap}: {arr}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # Print the array after each gap iteration
        print(f"After iteration {iteration} (gap {gap}): {arr}")
        gap //= 2
        iteration += 1
    
    return arr

# Input percentage data
n = int(input("Enter number of students: "))
percentages = []

for i in range(n):
    percent = float(input(f"Enter percentage for student {i + 1}: "))
    percentages.append(percent)

# Bubble Sort
print("\nPerforming Bubble Sort:")
bubble_sorted = bubble_sort(percentages.copy())  # Use a copy to preserve original list
print(f"Sorted array using Bubble Sort: {bubble_sorted}")

# Shell Sort
print("\nPerforming Shell Sort:")
shell_sorted = shell_sort(percentages.copy())  # Use a copy to preserve original list
print(f"Sorted array using Shell Sort: {shell_sorted}")




# Bubble Sort:

# Best case:O(n) (with optimization)
# Worst case: O(n^2)
# Outer loop: The outer loop runs n-1where ,n is the length of the array.
# Inner loop: The inner loop compares adjacent elements, and in the worst case, it runs n-1-i

# Shell Sort:

# Shell Sort is an optimized version of Insertion Sort that sorts elements in subgroups defined by a gap sequence. 
# It reduces the number of inversions by comparing elements that are far apart, progressively reducing the gap until it is 1

# Best case : O(nlogn)
# Worst case: O(n^2)
# Function to perform counting sort based on the digit represented by exp (1, 10, 100, ...)
def counting_sort(arr, exp):
    n = len(arr)
    
    # Output array to store sorted order
    output = [0] * n
    count = [0] * 10  # Since digits range from 0 to 9

    # Store count of occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Modify count array to store cumulative positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using cumulative count
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted numbers based on this digit back to arr
    for i in range(n):
        arr[i] = output[i]

# Function to perform Radix Sort
def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Perform counting sort for each digit, starting with least significant digit
    exp = 1  # Initialize exponent (1, 10, 100, etc.)
    iteration = 1
    
    while max_num // exp > 0:
        print(f"Before sorting by digit at exp {exp}: {arr}")
        counting_sort(arr, exp)
        print(f"After iteration {iteration} (exp {exp}): {arr}\n")
        exp *= 10
        iteration += 1

# Input number of students and their marks
n = int(input("Enter number of students: "))
marks = []

# Input student marks
for i in range(n):
    mark = int(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark)

# Display the original array
print("\nOriginal array of marks:", marks)

# Perform Radix Sort and display the array after each iteration
print("\nPerforming Radix Sort:")
radix_sort(marks)

# Display the final sorted array
print(f"Sorted array using Radix Sort: {marks}")



# Thus, the overall time complexity of counting_sort is O(n), where n is the number of elements in the array.

# radix sort:
# Since the number of iterations depends on the number of digits in the largest number,
# the overall time complexity of the Radix Sort algorithm is O(n⋅log base of 10(max_num)).
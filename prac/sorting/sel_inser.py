# Function to perform Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Selection Sort - Iteration {i + 1}: {arr}")  # Display array after each iteration

# Function to perform Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Insertion Sort - Iteration {i}: {arr}")  # Display array after each iteration

# Function to input student marks
def input_marks():
    n = int(input("Enter the number of students: "))
    marks = []
    for i in range(n):
        mark = int(input(f"Enter marks for student {i + 1}: "))
        marks.append(mark)
    return marks

# Main program
def main():
    marks = input_marks()
    
    
    print("\nOriginal array:", marks)
    
    # Selection Sort
    print("\nPerforming Selection Sort:")
    selection_sort(marks.copy())  # Pass a copy of the list to preserve the original

    # Insertion Sort
    print("\nPerforming Insertion Sort:")
    insertion_sort(marks.copy())  # Pass a copy of the list to preserve the original

if __name__ == "__main__":
    main()
    
    
    
    # 1. Selection Sort
    # Best case = Worst case = Average case = O(n^2)
    # Selection Sort always performs O(n^2) comparisons, regardless of whether the array is already sorted or not.


# Insertion Sort
# Best case:O(n)(when the array is already sorted)
# Worst case:O(n^2) (when the array is in reverse order)
# Average case: O(n^2)(for a randomly ordered array)

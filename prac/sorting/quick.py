# Function to perform Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)
        
        # Display the array after each partitioning iteration
        print(f"Iteration (Pivot at index {pi}): {arr}")
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Function to find the partition position
def partition(arr, low, high):
    pivot = arr[high]  # Pivot element (last element)
    i = low - 1  # Pointer for greater element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

# Function to input student marks
def input_marks():
    n = int(input("Enter the number of students: "))
    marks = []
    for i in range(n):
        mark = int(input(f"Enter marks for student {i + 1}: "))
        marks.append(mark)
    return marks

# Function to display the top 5 scores
def display_top_five(arr):
    top_scores = arr[-5:]  # Get the last 5 elements (highest scores)
    print("\nTop 5 scores:")
    for score in reversed(top_scores):  # Display in descending order
        print(score)

# Main program
def main():
    marks = input_marks()

    print("\nOriginal array:", marks)
    
    print("\nPerforming Quick Sort:")
    quick_sort(marks, 0, len(marks) - 1)
    
    print("\nSorted array:", marks)
    
    # Display top five scores
    display_top_five(marks)

if __name__ == "__main__":
    main()



# Best Case = Average Case = O(n⋅logn)
# Worst Case:O(n^2)
# To mitigate the worst-case performance, techniques like random pivot selection 
# or median-of-three pivot selection can be used to make the algorithm more robust in practice
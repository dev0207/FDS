# Part 1: Linear Search for Unsorted Array
def linear_search(arr, roll_number):
    for i in range(len(arr)):
        if arr[i] == roll_number:
            return True  # Student found
    return False  # Student not found

# Part 2: Fibonacci Search for Sorted Array
def fibonacci_search(arr, roll_number):
    n = len(arr)
    
    # Initialize the Fibonacci numbers
    fib_m_2 = 0  # (m-2)'th Fibonacci number
    fib_m_1 = 1  # (m-1)'th Fibonacci number
    fib = fib_m_1 + fib_m_2  # m'th Fibonacci number
    
    # Find the smallest Fibonacci number greater than or equal to n
    while fib < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib
        fib = fib_m_1 + fib_m_2
    
    # Now we have fib_m_1 as the closest Fibonacci number greater than or equal to n
    offset = -1
    
    while fib > 1:
        # Check if fib_m_2 is a valid index
        i = min(offset + fib_m_2, n - 1)
        
        # If roll_number is greater, move the range to the right
        if arr[i] < roll_number:
            fib = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib - fib_m_1
            offset = i
        
        # If roll_number is smaller, move the range to the left
        elif arr[i] > roll_number:
            fib = fib_m_2
            fib_m_1 = fib_m_1 - fib_m_2
            fib_m_2 = fib - fib_m_1
        
        # Found roll_number
        else:
            return True
    
    # Check if the last element is the roll_number
    if fib_m_1 and arr[offset + 1] == roll_number:
        return True
    
    return False

# Main function to test both searches
def main():
    # Taking user input for unsorted array (linear search)
    unsorted_roll_numbers = list(map(int, input("Enter roll numbers (unsorted, space-separated): ").split()))
    roll_number_to_search = int(input("Enter roll number to search: "))
    
    print("\nPart 1: Linear Search")
    if linear_search(unsorted_roll_numbers, roll_number_to_search):
        print(f"Roll number {roll_number_to_search} attended the training program.")
    else:
        print(f"Roll number {roll_number_to_search} did not attend the training program.")
    
    # Taking user input for sorted array (fibonacci search)
    sorted_roll_numbers = list(map(int, input("\nEnter roll numbers (sorted, space-separated): ").split()))
    
    print("\nPart 2: Fibonacci Search")
    if fibonacci_search(sorted_roll_numbers, roll_number_to_search):
        print(f"Roll number {roll_number_to_search} attended the training program.")
    else:
        print(f"Roll number {roll_number_to_search} did not attend the training program.")

# Run the program
main()

 


#  Linear Search (Unsorted Array)

# The linear_search function performs a linear scan of the array to find the target element (in this case, a student's roll number).
# It compares each element with the given roll number sequentially.In the worst case, the function has to scan through the entire array, 
# so the time complexity is proportional to the length of the array n.

# Time complexity: O(n), where n is the number of elements in the array 



#  Fibonacci Search (Sorted Array)

# The fibonacci_search function is a more advanced searching algorithm for sorted arrays. 
# It uses Fibonacci numbers to divide the search space,
# reducing the range of possible positions more efficiently than a simple linear search

# Time complexity: 𝑂(logn), where n is the number of elements in the array

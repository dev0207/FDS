# Function to perform binary search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid  # Return index of found key
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if key not found

# Function to input sorted roll numbers
def input_sorted_roll_numbers():
    n = int(input("Enter the number of students: "))
    arr = []
    for i in range(n):
        roll_no = int(input(f"Enter sorted roll number of student {i + 1}: "))
        arr.append(roll_no)
    return arr

# Main program
def main():
    arr = input_sorted_roll_numbers()

    key = int(input("Enter the roll number to search: "))
    result = binary_search(arr, key)

    if result != -1:
        print(f"Roll number {key} attended the training program (found at index {result}).")
    else:
        print(f"Roll number {key} did not attend the training program.")

if __name__ == "__main__":
    main()





# binary_search(): O(log n)
# input_sorted_roll_numbers(): O(n)
# Overall time complexity: O(n)
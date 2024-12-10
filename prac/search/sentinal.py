# Function to perform sentinel search
def sentinel_search(arr, n, key):
    last = arr[n - 1]
    arr[n - 1] = key
    i = 0

    while arr[i] != key:
        i += 1

    arr[n - 1] = last

    if i < n - 1 or arr[n - 1] == key:
        return i  # Return index of the found key
    else:
        return -1  # Return -1 if key not found

# Function to input roll numbers
def input_roll_numbers():
    n = int(input("Enter the number of students: "))
    arr = []
    for i in range(n):
        roll_no = int(input(f"Enter roll number of student {i + 1}: "))
        arr.append(roll_no)
    return arr, n

# Main program
def main():
    arr, n = input_roll_numbers()

    key = int(input("Enter the roll number to search: "))
    result = sentinel_search(arr, n, key)

    if result != -1:
        print(f"Roll number {key} attended the training program (found at index {result}).")
    else:
        print(f"Roll number {key} did not attend the training program.")

if __name__ == "__main__":
    main()


# Sentinel Search:
 
# Sentinel Search is an optimized version of linear search that avoids checking whether the index is within bounds during each iteration.
# Instead, it places the target value (key) at the end of the list (sentinel), which simplifies the loop termination condition.
# After searching, the sentinel value is restored.


# Best case: The key is found at the first index, so the loop will terminate after one comparison. Thus, the time complexity in the best case is 𝑂(1)

# Worst case: The key is either not in the array or it is at the last position. 
# The loop will iterate over all  elements (including the sentinel), resulting in a time complexity of O(n).

# Average case: On average, the key might be found around the middle of the array, so the time complexity will still be O(n).
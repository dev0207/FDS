import numpy as np

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Function to check if the matrix is upper triangular
def is_upper_triangular(matrix):
    rows, cols = matrix.shape
    for i in range(1, rows):
        for j in range(i):
            if matrix[i, j] != 0:
                return False
    return True

# Function to check if the matrix is a magic square
def is_magic_square(matrix):
    n = matrix.shape[0]
    # Check if matrix contains all numbers from 1 to n^2
    elements = np.sort(matrix.flatten())
    if not np.array_equal(elements, np.arange(1, n*n+1)):
        return False
    
    # Sum of the first row (or any row) to compare with other sums
    magic_sum = np.sum(matrix[0, :])

    # Check row sums
    for i in range(n):
        if np.sum(matrix[i, :]) != magic_sum:
            return False

    # Check column sums
    for j in range(n):
        if np.sum(matrix[:, j]) != magic_sum:
            return False

    # Check diagonal sums
    if np.sum(np.diag(matrix)) != magic_sum or np.sum(np.diag(np.fliplr(matrix))) != magic_sum:
        return False

    return True

# Function to take input from user and form a matrix
def input_matrix():
    n = int(input("Enter the number of rows/columns for the matrix: "))
    matrix = []
    print(f"Enter the elements of the matrix (row by row):")
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

# Main program
def main():
    print("Enter details for matrix 1:")
    matrix1 = input_matrix()
    
    print("Enter details for matrix 2:")
    matrix2 = input_matrix()
    
    print("\nAddition of matrices:")
    print(add_matrices(matrix1, matrix2))
    
    print("\nMultiplication of matrices:")
    print(multiply_matrices(matrix1, matrix2))

    print("\nCheck if Matrix 1 is Upper Triangular:")
    if is_upper_triangular(matrix1):
        print("Matrix 1 is upper triangular.")
    else:
        print("Matrix 1 is not upper triangular.")
    
    print("\nCheck if Matrix 1 is a Magic Square:")
    if is_magic_square(matrix1):
        print("Matrix 1 is a magic square.")
    else:
        print("Matrix 1 is not a magic square.")

if __name__ == "__main__":
    main()



# Overall Time Complexity:
# Matrix Addition (add_matrices): O(n²)
# Matrix Multiplication (multiply_matrices): O(n³)
# Check Upper Triangular (is_upper_triangular): O(n²)
# Check Magic Square (is_magic_square): O(n² log n)
# Matrix Input (input_matrix): O(n²)

# the overall time complexity of the program is dominated by the matrix multiplication function (multiply_matrices),
# which has a complexity of O(n³). Therefore, the overall time complexity of the program is O(n³).
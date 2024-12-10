import numpy as np

# Function to compute the transpose of a matrix
def transpose_matrix(matrix):
    return np.transpose(matrix)

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Function to find the saddle point
def find_saddle_point(matrix):
    rows, cols = matrix.shape
    saddle_points = []

    for i in range(rows):
        # Find the minimum value in the ith row
        row_min = np.min(matrix[i, :])
        col_index = np.argmin(matrix[i, :])

        # Check if it's the largest value in its column
        if row_min == np.max(matrix[:, col_index]):
            saddle_points.append((i, col_index, row_min))

    return saddle_points

# Function to take input from user and form a matrix
def input_matrix():
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))
    matrix = []
    print(f"Enter the elements of the matrix (row by row):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

# Main program
def main():
    print("Enter details for matrix 1:")
    matrix1 = input_matrix()

    print("\nTranspose of Matrix 1:")
    print(transpose_matrix(matrix1))

    print("\nEnter details for matrix 2:")
    matrix2 = input_matrix()

    if matrix1.shape == matrix2.shape:
        print("\nAddition of matrices:")
        print(add_matrices(matrix1, matrix2))
    else:
        print("\nMatrix addition is not possible (shape mismatch).")

    if matrix1.shape[1] == matrix2.shape[0]:
        print("\nMultiplication of matrices:")
        print(multiply_matrices(matrix1, matrix2))
    else:
        print("\nMatrix multiplication is not possible (shape mismatch).")

    print("\nFinding saddle points in Matrix 1:")
    saddle_points = find_saddle_point(matrix1)
    if saddle_points:
        for (i, j, val) in saddle_points:
            print(f"Saddle point found at row {i+1}, column {j+1} with value {val}.")
    else:
        print("No saddle point found in Matrix 1.")

if __name__ == "__main__":
    main()



# The transpose operation has 𝑂(𝑚×𝑛)
# The matrix addition has O(m×n).
# The matrix multiplication has O(m×p×n), which can vary depending on the dimensions of the matrices.
# The saddle point detection has O(m×n).
# The matrix input takes O(m×n)


# Final Time Complexity Summary:
# Overall Time Complexity: O(m×n) for most operations, except for matrix multiplication, which is O(m×p×n).
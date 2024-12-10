# Class to represent a sparse matrix
class SparseMatrix:
    def __init__(self, rows, cols, elements):
        self.rows = rows  # Number of rows
        self.cols = cols  # Number of columns
        self.elements = elements  # List of [row, col, value] for non-zero elements

    # Function to display the sparse matrix
    def display(self):
        print(f"Sparse Matrix Representation: [row, col, value]")
        for element in self.elements:
            print(f"[{element[0]}, {element[1]}, {element[2]}]")

    # Simple Transpose: swaps row and column for each element
    def simple_transpose(self):
        transposed_elements = []
        for element in self.elements:
            transposed_elements.append([element[1], element[0], element[2]])  # Swap row and col
        # Sort by row and column for proper order after transposing
        transposed_elements.sort(key=lambda x: (x[0], x[1]))
        return SparseMatrix(self.cols, self.rows, transposed_elements)

    # Function to add two sparse matrices
    @staticmethod
    def add_matrices(matrix1, matrix2):
        if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
            print("Matrices cannot be added. They have different dimensions.")
            return None
        
        result_elements = []
        i, j = 0, 0
        while i < len(matrix1.elements) and j < len(matrix2.elements):
            r1, c1, v1 = matrix1.elements[i]
            r2, c2, v2 = matrix2.elements[j]

            if r1 == r2 and c1 == c2:
                # Same position, so we add the values
                result_elements.append([r1, c1, v1 + v2])
                i += 1
                j += 1
            elif r1 < r2 or (r1 == r2 and c1 < c2):
                # Take element from matrix1
                result_elements.append([r1, c1, v1])
                i += 1
            else:
                # Take element from matrix2
                result_elements.append([r2, c2, v2])
                j += 1

        # Append remaining elements from matrix1 or matrix2
        while i < len(matrix1.elements):
            result_elements.append(matrix1.elements[i])
            i += 1
        while j < len(matrix2.elements):
            result_elements.append(matrix2.elements[j])
            j += 1

        return SparseMatrix(matrix1.rows, matrix1.cols, result_elements)

# Function to create a sparse matrix from user input
def create_sparse_matrix():
    rows = int(input("Enter number of rows in the matrix: "))
    cols = int(input("Enter number of columns in the matrix: "))
    num_non_zero = int(input("Enter the number of non-zero elements: "))
    
    elements = []
    for _ in range(num_non_zero):
        r = int(input("Enter row index (0-based): "))
        c = int(input("Enter column index (0-based): "))
        v = int(input("Enter value: "))
        elements.append([r, c, v])

    return SparseMatrix(rows, cols, elements)

# Main function
def main():
    print("Input first sparse matrix:")
    matrix1 = create_sparse_matrix()
    print("\nOriginal Sparse Matrix 1:")
    matrix1.display()

    print("\nInput second sparse matrix:")
    matrix2 = create_sparse_matrix()
    print("\nOriginal Sparse Matrix 2:")
    matrix2.display()

    # Perform Simple Transpose of matrix1
    transposed_matrix = matrix1.simple_transpose()
    print("\nSimple Transpose of the first Sparse Matrix:")
    transposed_matrix.display()

    # Perform Addition of matrix1 and matrix2
    added_matrix = SparseMatrix.add_matrices(matrix1, matrix2)
    if added_matrix:
        print("\nAddition of the two Sparse Matrices:")
        added_matrix.display()

if __name__ == "__main__":
    main()



# the overall time complexity for the most significant operations in the code is:
# for transposing a matrix: O(k log k)
# For adding two matrices: O(k1 + k2) (where k1 and k2 are the number of non-zero elements in the two matrices)

# In general, the time complexity of the sparse matrix operations is dominated by the number of non-zero elements in the matrix,
# and for each operation, it's linear or logarithmic in the number of non-zero elements.
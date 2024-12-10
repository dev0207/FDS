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

    # Simple Transpose
    def simple_transpose(self):
        transposed_elements = []
        for element in self.elements:
            transposed_elements.append([element[1], element[0], element[2]])  # Swap row and col
        # Sort by row and column for proper order after transposing
        transposed_elements.sort(key=lambda x: (x[0], x[1]))
        return SparseMatrix(self.cols, self.rows, transposed_elements)

    # Fast Transpose
    def fast_transpose(self):
        row_terms = [0] * self.cols
        starting_pos = [0] * self.cols
        transposed_elements = [[0, 0, 0]] * len(self.elements)

        # Step 1: Count the number of elements in each column (row in transposed matrix)
        for element in self.elements:
            row_terms[element[1]] += 1

        # Step 2: Calculate starting position for each column in transposed matrix
        starting_pos[0] = 0
        for i in range(1, self.cols):
            starting_pos[i] = starting_pos[i - 1] + row_terms[i - 1]

        # Step 3: Place elements in correct position in transposed matrix
        for element in self.elements:
            col = element[1]
            pos = starting_pos[col]
            transposed_elements[pos] = [element[1], element[0], element[2]]  # Swap row and col
            starting_pos[col] += 1

        return SparseMatrix(self.cols, self.rows, transposed_elements)

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
    sparse_matrix = create_sparse_matrix()
    print("\nOriginal Sparse Matrix:")
    sparse_matrix.display()

    # Perform Simple Transpose
    simple_transposed = sparse_matrix.simple_transpose()
    print("\nSimple Transpose of the Sparse Matrix:")
    simple_transposed.display()

    # Perform Fast Transpose
    fast_transposed = sparse_matrix.fast_transpose()
    print("\nFast Transpose of the Sparse Matrix:")
    fast_transposed.display()

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    # Time complexity of simple transpose=O(nlogn)
    # Time complexity of fast transpose=O(n+m)
    # Display: O(n)
    # In the worst case, for large matrices with many non-zero elements, the fast transpose will likely be more efficient than the simple transpose
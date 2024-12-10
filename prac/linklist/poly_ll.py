class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient  # Coefficient of the term
        self.exponent = exponent        # Exponent of the term
        self.next = None                # Next pointer in the linked list


class Polynomial:
    def __init__(self):
        self.head = None  # Head of the linked list

    # Function to insert a new term in the polynomial
    def insert_term(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if not self.head:
            self.head = new_node
        else:
            # Insert the new term in the sorted order based on the exponent
            temp = self.head
            while temp.next and temp.next.exponent > exponent:
                temp = temp.next
            if temp.next and temp.next.exponent == exponent:
                temp.next.coefficient += coefficient  # Combine like terms
            else:
                new_node.next = temp.next
                temp.next = new_node

    # Function to display the polynomial
    def display(self):
        temp = self.head
        while temp:
            if temp.coefficient > 0 and temp != self.head:
                print(f"+{temp.coefficient}x^{temp.exponent}", end=" ")
            else:
                print(f"{temp.coefficient}x^{temp.exponent}", end=" ")
            temp = temp.next
        print()

    # Function to evaluate the polynomial at a given value of x
    def evaluate(self, x):
        result = 0
        temp = self.head
        while temp:
            result += temp.coefficient * (x ** temp.exponent)
            temp = temp.next
        return result

    # Function to add two polynomials
    def add_polynomials(self, other_poly):
        result_poly = Polynomial()
        p1 = self.head
        p2 = other_poly.head

        while p1 and p2:
            if p1.exponent > p2.exponent:
                result_poly.insert_term(p1.coefficient, p1.exponent)
                p1 = p1.next
            elif p2.exponent > p1.exponent:
                result_poly.insert_term(p2.coefficient, p2.exponent)
                p2 = p2.next
            else:  # If exponents are the same, add coefficients
                result_poly.insert_term(p1.coefficient + p2.coefficient, p1.exponent)
                p1 = p1.next
                p2 = p2.next

        # Add remaining terms of p1
        while p1:
            result_poly.insert_term(p1.coefficient, p1.exponent)
            p1 = p1.next

        # Add remaining terms of p2
        while p2:
            result_poly.insert_term(p2.coefficient, p2.exponent)
            p2 = p2.next

        return result_poly


# Driver code to test the implementation
def main():
    poly1 = Polynomial()
    poly2 = Polynomial()

    # Get the number of terms for the first polynomial
    n1 = int(input("Enter the number of terms in the first polynomial: "))
    print("Enter the terms (coefficient exponent):")
    for _ in range(n1):
        coefficient, exponent = map(int, input().split())
        poly1.insert_term(coefficient, exponent)

    # Get the number of terms for the second polynomial
    n2 = int(input("Enter the number of terms in the second polynomial: "))
    print("Enter the terms (coefficient exponent):")
    for _ in range(n2):
        coefficient, exponent = map(int, input().split())
        poly2.insert_term(coefficient, exponent)

    print("First Polynomial:")
    poly1.display()

    print("Second Polynomial:")
    poly2.display()

    # Add the polynomials
    result_poly = poly1.add_polynomials(poly2)
    print("Sum of the Polynomials:")
    result_poly.display()

    # Evaluate the first polynomial at x = 2
    x_value = float(input("Enter the value of x to evaluate the first polynomial: "))
    print(f"First Polynomial evaluated at x = {x_value}: {poly1.evaluate(x_value)}")

    # Evaluate the second polynomial at x = 2
    print(f"Second Polynomial evaluated at x = {x_value}: {poly2.evaluate(x_value)}")


if __name__ == "__main__":
    main()



# Insert Term:O(n)
# Display: O(n)
# Evaluate: O(n)
# Add Polynomials:O(n+m)

# In summary, the most expensive operations are insertion and addition,
# both of which are linear in the number of terms, making the overall complexity of polynomial operations O(n)
# (where n is the number of terms in a polynomial). For adding two polynomials,
# it is O(n+m), where n and m are the numbers of terms in each polynomial.

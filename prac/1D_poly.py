# Function to input a polynomial
def input_polynomial():
    degree = int(input("Enter the degree of the polynomial: "))
    coeffs = []
    for i in range(degree, -1, -1):
        coeff = float(input(f"Enter coefficient for x^{i}: "))
        coeffs.append(coeff)
    return coeffs

# Function to output a polynomial
def output_polynomial(coeffs):
    polynomial = ""
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        power = degree - i
        if coeff != 0:
            if power > 0:
                polynomial += f"{coeff}x^{power} + "
            else:
                polynomial += f"{coeff}"
    print("Polynomial: ", polynomial)

# Function to evaluate a polynomial at a given value of x
def evaluate_polynomial(coeffs, x):
    result = 0
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        result += coeff * (x ** (degree - i))
    return result

# Function to add two polynomials
def add_polynomials(p1, p2):
    # Make both polynomials of the same size by padding the smaller one with zeros
    if len(p1) > len(p2):
        p2 = [0] * (len(p1) - len(p2)) + p2
    elif len(p2) > len(p1):
        p1 = [0] * (len(p2) - len(p1)) + p1
    
    result = [p1[i] + p2[i] for i in range(len(p1))]
    return result

# Function to multiply two polynomials
def multiply_polynomials(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    
    return result

# Main program
def main():
    print("Input first polynomial:")
    p1 = input_polynomial()
    output_polynomial(p1)
    
    print("\nInput second polynomial:")
    p2 = input_polynomial()
    output_polynomial(p2)
    
    # Polynomial Evaluation
    x = float(input("\nEnter the value of x to evaluate the first polynomial: "))
    value = evaluate_polynomial(p1, x)
    print(f"The value of the first polynomial at x = {x} is {value}")

    # Adding two polynomials
    added_polynomial = add_polynomials(p1, p2)
    print("\nThe result of adding the two polynomials is:")
    output_polynomial(added_polynomial)
    
    # Multiplying two polynomials
    multiplied_polynomial = multiply_polynomials(p1, p2)
    print("\nThe result of multiplying the two polynomials is:")
    output_polynomial(multiplied_polynomial)

if __name__ == "__main__":
    main()



# Overall Time Complexity:

# input_polynomial(): O(d), where d is the degree of the polynomial.
# output_polynomial(): O(n), where n is the number of terms (or degree + 1).
# evaluate_polynomial(): O(n), where n is the number of terms (or degree + 1).
# add_polynomials(): O(n), where n is the maximum size of the two polynomials.
# multiply_polynomials(): O(n1 * n2), where n1 and n2 are the number of terms in the two polynomials.

# Thus, the overall time complexity is dominated by the polynomial multiplication step, which has a time complexity of O(n1 * n2)
# Function to input a polynomial
def input_polynomial():
    terms = int(input("Enter number of terms in the polynomial: "))
    polynomial = []
    
    for i in range(terms):
        coeff = int(input(f"Enter coefficient of term {i + 1}: "))
        exp = int(input(f"Enter exponent of term {i + 1}: "))
        polynomial.append([coeff, exp])
    
    return polynomial

# Function to output a polynomial
def output_polynomial(polynomial):
    result = ""
    for term in polynomial:
        coeff, exp = term
        if exp == 0:
            result += f"{coeff}"
        else:
            result += f"{coeff}x^{exp}"
        
        if term != polynomial[-1]:
            result += " + "
    
    print(f"Polynomial: {result}")

# Function to evaluate a polynomial at a given value of x
def evaluate_polynomial(polynomial, x):
    result = 0
    for coeff, exp in polynomial:
        result += coeff * (x ** exp)
    return result

# Function to add two polynomials
def add_polynomials(poly1, poly2):
    result = []
    i, j = 0, 0
    while i < len(poly1) and j < len(poly2):
        if poly1[i][1] > poly2[j][1]:  # Compare exponents
            result.append(poly1[i])
            i += 1
        elif poly1[i][1] < poly2[j][1]:
            result.append(poly2[j])
            j += 1
        else:
            # If exponents are equal, add the coefficients
            result.append([poly1[i][0] + poly2[j][0], poly1[i][1]])
            i += 1
            j += 1
    
    # Append the remaining terms
    while i < len(poly1):
        result.append(poly1[i])
        i += 1
    while j < len(poly2):
        result.append(poly2[j])
        j += 1
    
    return result

# Function to multiply two polynomials
def multiply_polynomials(poly1, poly2):
    result = {}
    
    for coeff1, exp1 in poly1:
        for coeff2, exp2 in poly2:
            new_coeff = coeff1 * coeff2
            new_exp = exp1 + exp2
            if new_exp in result:
                result[new_exp] += new_coeff
            else:
                result[new_exp] = new_coeff
    
    # Convert the result dictionary to a sorted list of terms
    result_polynomial = [[coeff, exp] for exp, coeff in result.items()]
    result_polynomial.sort(key=lambda term: -term[1])  # Sort by exponent in descending order
    
    return result_polynomial

# Main program
def main():
    print("Input first polynomial:")
    poly1 = input_polynomial()
    output_polynomial(poly1)

    print("\nInput second polynomial:")
    poly2 = input_polynomial()
    output_polynomial(poly2)

    # Evaluate first polynomial at a given value of x
    x_val = int(input("\nEnter value of x to evaluate the first polynomial: "))
    result = evaluate_polynomial(poly1, x_val)
    print(f"Result of evaluating first polynomial at x = {x_val}: {result}")

    # Add two polynomials
    added_polynomial = add_polynomials(poly1, poly2)
    print("\nResult of adding the two polynomials:")
    output_polynomial(added_polynomial)

    # Multiply two polynomials
    multiplied_polynomial = multiply_polynomials(poly1, poly2)
    print("\nResult of multiplying the two polynomials:")
    output_polynomial(multiplied_polynomial)

if __name__ == "__main__":
    main()



# input_polynomial(): O(n), where n is the number of terms in the polynomial.
# output_polynomial(): O(n), where n is the number of terms in the polynomial.
# evaluate_polynomial(): O(n), where n is the number of terms in the polynomial.
# add_polynomials(): O(n + m), where n and m are the number of terms in the first and second polynomial, respectively.
# multiply_polynomials(): O(n * m), where n and m are the number of terms in the first and second polynomial, respectively.

# Thus, the overall time complexity is dominated by the polynomial multiplication step, which has a time complexity of O(n * m).
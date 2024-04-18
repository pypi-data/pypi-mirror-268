"""
polynomial_generator/polynomial.py

A Python module for generating polynomial expressions based on the specified variables and degree.

Author: Hermann Agossou
Date: 2024/04/11
"""

from itertools import product


def generate_polynomial_expression(variables, degree):
    """
    Generate a polynomial expression for a given list of variables and degree.

    Args:
        variables (list): A list of variable names as strings.
        degree (int): The degree of the polynomial.

    Returns:
        tuple: A tuple containing the first term of the polynomial and the full polynomial expression.
               The first term represents the binomial expansion of the variables raised to the given degree.
    Example:
        >>> variables = ['x', 'y', 'z']
        >>> degree = 2
        >>> generate_polynomial(variables, degree)
        "('x + y + z)^2', 'x^2 + x*y + x*z + y^2 + y*z + z^2'"
    """

    variables = [elt.strip() for elt in variables]

    # Generate all possible combinations of exponents for the variables
    combinations = product(range(degree + 1), repeat=len(variables))

    # Filter combinations to include only those whose exponents sum up to the given degree
    combinations = filter(lambda x: sum(x) == degree, combinations)

    # Initialize the polynomial expression
    expression = ""

    # Iterate over each combination of exponents
    for combination in combinations:
        # Generate terms for the current combination
        terms = [
            f"{var}" if exp == 1 else f"{var}^{exp}" if exp > 1 else None
            for (exp, var) in zip(combination, variables)
        ]
        terms = filter(lambda x: x, terms)  # Remove None values
        # Join the terms with '*' and add them to the polynomial expression
        expression = "*".join(terms) + " + " + expression

    # Removing the trailing " + " from the last term
    expression = expression.rstrip("+ ")

    # Generate the first term of the polynomial
    first_term = f"({' + '.join(variables)})^{degree}"

    return first_term, expression


# Example usage:
if __name__ == "__main__":
    variables = ["x", "y", "z", "t"]
    nb_var = 3
    variables = variables[:nb_var]
    degree = 2
    first_term, expression = generate_polynomial_expression(variables, degree)
    print(f"{first_term} = {expression}")

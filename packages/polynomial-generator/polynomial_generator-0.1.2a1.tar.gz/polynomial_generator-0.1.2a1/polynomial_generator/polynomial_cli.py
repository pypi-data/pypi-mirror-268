"""
polynomial_generator/polynomial_cli.py
Author: Hermann Agossou
Date: 2024/04/11
"""

import argparse

from polynomial_generator import generate_polynomial_expression


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Generate polynomial expressions.")
    parser.add_argument(
        "-v", "--variables", default="x,y,z", help="Comma-separated list of variables"
    )
    parser.add_argument(
        "-d", "--degree", type=int, default=2, help="Degree of the polynomial"
    )

    # Parse arguments
    args = parser.parse_args()

    variables = args.variables.split(",")
    degree = args.degree

    _, polynomial = generate_polynomial_expression(variables, degree)

    print(f"variables: {variables}")
    print(f"degree: {degree}")

    print(f"Polynomial: {polynomial}")


if __name__ == "__main__":
    main()

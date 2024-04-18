# Polynomial Generator

[![License](https://img.shields.io/github/license/hermann-web/polynomial-generator)](LICENSE)
[![Release](https://img.shields.io/github/v/release/hermann-web/polynomial-generator)](https://github.com/hermann-web/polynomial-generator/releases)

## Overview

Polynomial Generator is a Python package that provides a command-line interface (CLI) application and a graphical user interface (GUI) application for generating polynomial expressions. It allows users to specify variables and degrees to create custom polynomials effortlessly.

## Features

- Generate polynomial expressions with custom variables and degrees.
- Cross-platform compatibility (Linux, Mac, Windows).
- Simple and intuitive user interface.

## Installation

You can install the Polynomial Generator package using pip:

```bash
pip install polynomial-generator
```

## Command-Line Interface (CLI)

You can use the CLI script to generate polynomials from the command line. Here's how to use it:

```bash
polygen -v <variables> -d <degree>
```

Replace `<variables>` with a comma-separated list of variables and `<degree>` with the desired degree of the polynomial. If no arguments are provided, default values (x,y,z for variables and 2 for degree) will be used.

Example:

```bash
polygen -v x,y,z -d 3
```

Output:

```plaintext
variables: ['x', 'y', 'z']
degree: 3
Polynomial: x^3 + x^2*y + x^2*z + x*y^2 + x*y*z + x*z^2 + y^3 + y^2*z + y*z^2 + z^3
```

## Using the Function in Your Python Scripts

Alternatively, you can use the `generate_polynomial_expression` function directly in your Python scripts. Here's how to import and use it:

```python
from polynomial_generator import generate_polynomial_expression

variables = ['x', 'y', 'z']
degree = 2

first_term, polynomial = generate_polynomial_expression(variables, degree)

print(f"Polynomial: {first_term} --> {polynomial}")
# output: Polynomial: (x + y + z)^2 --> x^2 + x*y + x*z + y^2 + y*z + z^2
```

## Graphical User Interface (GUI)

After installation, you can run the Polynomial Generator GUI application using the following command:

```bash
polygenapp
```

Enter the variables and degree for your polynomial, then click "Generate" to see the result.

![GUI Frontend](https://raw.githubusercontent.com/Hermann-web/polynomial-generator/main/assets/polygenapp-example.png)

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, feel free to contact [Hermann Agossou](mailto:agossouhermann7@gmail.com).

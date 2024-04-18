"""
polynomial_generator/polynomial_app.py

Polynomial Generator Application

This application allows users to generate polynomial expressions based on specified variables and degree.

Author: Hermann Agossou
Date: 2024/04/11
"""

import tkinter as tk
from tkinter import ttk

from polynomial_generator import generate_polynomial_expression


class PolynomialGeneratorApp:
    """
    GUI application for generating polynomial expressions.
    """

    def __init__(self, root):
        """
        Initialize the PolynomialGeneratorApp.

        Parameters:
            root (tk.Tk): The root window for the application.
        """
        self.root = root
        self.root.title("Polynomial Generator")

        # Default values
        self.default_variables = "x,y,z"
        self.default_degree = "2"

        # Labels and Entry widgets for variables and degree
        self.variables_label = ttk.Label(root, text="Variables:")
        self.variables_label.grid(row=0, column=0, padx=5, pady=5)
        self.variables_entry = ttk.Entry(root, text=self.default_variables)
        self.variables_entry.insert(0, self.default_variables)
        self.variables_entry.grid(row=0, column=1, padx=5, pady=5)

        self.degree_label = ttk.Label(root, text="Degree:")
        self.degree_label.grid(row=1, column=0, padx=5, pady=5)
        self.degree_entry = ttk.Entry(root, text=self.default_degree)
        self.degree_entry.insert(0, self.default_degree)
        self.degree_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button for generating polynomial
        self.generate_button = ttk.Button(
            root, text="Generate", command=self.generate_polynomial
        )
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Label and Text widget for displaying result polynomial
        self.result_label = ttk.Label(root, text="Polynomial:")
        self.result_label.grid(row=3, column=0, padx=5, pady=5)
        self.result_text = tk.Text(root, height=4, width=50)
        self.result_text.grid(row=3, column=1, padx=5, pady=5)

    def generate_polynomial(self):
        """
        Generate polynomial expression based on user input variables and degree.
        """
        variables = (
            self.variables_entry.get().split(",")
            if self.variables_entry.get()
            else self.default_variables.split(",")
        )
        degree = (
            int(self.degree_entry.get())
            if self.degree_entry.get()
            else int(self.default_degree)
        )

        first_term, polynomial = generate_polynomial_expression(variables, degree)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, first_term + " --> " + polynomial)


def main():
    """
    Main function to create and run the PolynomialGeneratorApp.
    """
    root = tk.Tk()
    app = PolynomialGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

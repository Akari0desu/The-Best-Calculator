#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:48:09 2025

@author: jaspersdocument
"""

import tkinter as tk
from tkinter import messagebox
from calculator import Calculator  # Import calculation logic module

# Define UI colors and styles
BG_COLOR = "#222831"  # Background color (dark theme)
DISPLAY_COLOR = "#393E46"  # Display area background color
BTN_COLOR = "#FFFFFF"  # Button color (white)
BTN_TEXT_COLOR = "#000000"  # Button text color (black)
BTN_HIGHLIGHT = "#00ADB5"  # Button highlight color (cyan)
FONT_LARGE = ("Arial", 22, "bold")  # Font for display area
FONT_MEDIUM = ("Arial", 18, "bold")  # Font size for buttons

class CalculatorGUI:
    def __init__(self, root):
        """Initialize the Calculator GUI"""
        self.root = root
        self.root.title("Scientific Calculator")  # Set window title
        self.root.geometry("400x600")  # Set window size
        self.root.configure(bg=BG_COLOR)  # Set background color

        self.expression = ""  # Stores user input and expressions

        # Display area (Text field for showing expressions and results)
        self.display = tk.Entry(
            root, font=FONT_LARGE, bg=DISPLAY_COLOR, fg=BTN_TEXT_COLOR, 
            justify="right", bd=10, relief=tk.FLAT
        )
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=8, pady=15, sticky="ew")
        self.display.insert(0, "Please use mouse only")  # Initial instruction message

        # Button layout (Numeric, operations, trigonometric, and special functions)
        button_layout = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["sin", "cos", "tan", "sqrt"],
            ["arcsin", "arccos", "arctan", "^"],
            ["(", ")", "=", "DEL"]
        ]

        # Create buttons and arrange them in the grid layout
        for row_idx, row in enumerate(button_layout, start=1):
            for col_idx, btn_text in enumerate(row):
                button = tk.Button(
                    root, text=btn_text, font=FONT_MEDIUM, 
                    bg=BTN_COLOR, fg=BTN_TEXT_COLOR,  # White buttons with black text
                    activebackground=BTN_HIGHLIGHT, activeforeground=BTN_TEXT_COLOR,
                    relief=tk.RAISED, bd=3, padx=10, pady=10,
                    command=lambda text=btn_text: self.on_button_click(text)  # Assign function to button
                )
                button.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
        
        # Make buttons and window size adaptive
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)  # Adjust row spacing dynamically
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)  # Adjust column spacing dynamically

    def on_button_click(self, button_text):
        """Handles button click events and updates the expression"""
        if button_text == "=":
            self.calculate_result()  # Evaluate the expression
        elif button_text == "C":
            self.expression = ""  # Clear the expression
        elif button_text == "DEL":
            self.expression = self.expression[:-1]  # Remove the last character
        elif button_text == "sqrt":
            self.expression += "Calculator.square_root("  # Use Calculator function for square root
        elif button_text == "^":
            self.expression += "**"  # Exponentiation operator
        elif button_text in ["sin", "cos", "tan", "arcsin", "arccos", "arctan"]:
            # Mapping standard names to Calculator function names
            trig_map = {
                "sin": "sine",
                "cos": "cosine",
                "tan": "tangent",
                "arcsin": "arcsin",
                "arccos": "arccos",
                "arctan": "arctan"
            }
            self.expression += f"Calculator.{trig_map[button_text]}("
        else:
            self.expression += button_text  # Append numbers and other operators

        self.update_display()  # Refresh display area

    def calculate_result(self):
        """Evaluates the mathematical expression using the Calculator module"""
        try:
            # Ensure the number of opening and closing parentheses match
            if self.expression.count("(") > self.expression.count(")"):
                self.expression += ")" * (self.expression.count("(") - self.expression.count(")"))
            
            # Prevent division by zero
            if "/0" in self.expression:
                raise ZeroDivisionError
            
            # Evaluate the expression using Calculator module and Python's eval()
            result = eval(self.expression, {"Calculator": Calculator, "math": __import__("math")})

            # Check for error messages in result
            if result in ["Error: Division by zero", "Error: Cannot calculate the root of a negative number"]:
                raise ValueError(result)  # Raise an error so it can be caught below
            
            self.expression = str(result)  # Store the result as a string
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed")
            self.expression = ""  # Clear the expression after error
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Show the specific error message
            self.expression = ""
        except Exception:
            messagebox.showerror("Error", "Invalid Calculation")  # Generic error message
            self.expression = ""
        
        self.update_display()  # Refresh display after calculation

    def update_display(self):
        """Updates the calculator display to show the current expression"""
        self.display.delete(0, tk.END)  # Clear the display
        self.display.insert(tk.END, self.expression)  # Insert updated expression

def run_gui():
    """Runs the calculator GUI application"""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()  # Start the Tkinter main event loop

if __name__ == "__main__":
    run_gui()  # Launch the GUI when the script is executed
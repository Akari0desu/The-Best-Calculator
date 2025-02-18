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
BG_COLOR = "#222831"  # Background color (dark)
DISPLAY_COLOR = "#393E46"  # Display area background
BTN_COLOR = "#FFFFFF"  # Button color (black)
BTN_TEXT_COLOR = "#000000"  # Button text color (white)
BTN_HIGHLIGHT = "#00ADB5"  # Button highlight color (cyan)
FONT_LARGE = ("Arial", 22, "bold")  # Font for display
FONT_MEDIUM = ("Arial", 18, "bold")  # Button font size

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg=BG_COLOR)

        self.expression = ""
        
        # Display area
        self.display = tk.Entry(
            root, font=FONT_LARGE, bg=DISPLAY_COLOR, fg=BTN_TEXT_COLOR, 
            justify="right", bd=10, relief=tk.FLAT
        )
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=8, pady=15, sticky="ew")
        self.display.insert(0, "Please use mouse only")

        # Button layout
        button_layout = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["sin", "cos", "tan", "sqrt"],
            ["arcsin", "arccos", "arctan", "^"],
            ["(", ")", "=", "DEL"]
        ]

        # Create buttons
        for row_idx, row in enumerate(button_layout, start=1):
            for col_idx, btn_text in enumerate(row):
                button = tk.Button(
                    root, text=btn_text, font=FONT_MEDIUM, 
                    bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
                    activebackground=BTN_HIGHLIGHT, activeforeground=BTN_TEXT_COLOR,
                    relief=tk.RAISED, bd=3, padx=10, pady=10,
                    command=lambda text=btn_text: self.on_button_click(text)
                )
                button.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
        
        # Make buttons and window size adaptive
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        """Handles button clicks"""
        if button_text == "=":
            self.calculate_result()
        elif button_text == "C":
            self.expression = ""
        elif button_text == "DEL":
            self.expression = self.expression[:-1]
        elif button_text == "sqrt":
            self.expression += "math.sqrt("
        elif button_text == "^":
            self.expression += "**"
        elif button_text in ["sin", "cos", "tan", "arcsin", "arccos", "arctan"]:
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
            self.expression += button_text

        self.update_display()

    def calculate_result(self):
        """Evaluates the expression using the Calculator module"""
        try:
            if self.expression.count("(") > self.expression.count(")"):
                self.expression += ")" * (self.expression.count("(") - self.expression.count(")"))
            
            if "/0" in self.expression:
                raise ZeroDivisionError
            
            result = eval(self.expression, {"Calculator": Calculator, "math": __import__("math")})
            
            if result == "Error: Division by zero":
                raise ZeroDivisionError
            
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed")
            self.expression = ""
        except Exception:
            messagebox.showerror("Error", "Invalid Calculation")
            self.expression = ""
        self.update_display()

    def update_display(self):
        """Updates the display box"""
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

def run_gui():
    """Runs the calculator GUI"""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()

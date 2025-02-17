#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:31:42 2025

@author: jaspersdocument
"""

# -*- coding: utf-8 -*-
"""
GUI Module: Implements the calculator interface using Tkinter
"""

import tkinter as tk
from tkinter import messagebox
from calculator import Calculator  # Import the backend calculations

# Define colors and styles for the UI
BG_COLOR = "#222831"
FG_COLOR = "#EEEEEE"
BTN_COLOR = "#393E46"
BTN_HIGHLIGHT = "#00ADB5"
FONT_LARGE = ("Arial", 20, "bold")
FONT_MEDIUM = ("Arial", 14)

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg=BG_COLOR)

        self.expression = ""
        
        # Display area
        self.display = tk.Entry(root, font=FONT_LARGE, bg=BG_COLOR, fg=FG_COLOR, justify="right", bd=10, relief=tk.FLAT)
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=20, sticky="ew")
        self.display.bind("<Key>", self.key_press)  # Enable keyboard input
        self.display.focus_set()

        # Buttons layout
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
                    root, text=btn_text, font=FONT_MEDIUM, bg=BTN_COLOR, fg=FG_COLOR,
                    activebackground=BTN_HIGHLIGHT, relief=tk.RAISED, bd=3, padx=10, pady=10,
                    command=lambda text=btn_text: self.on_button_click(text)
                )
                button.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
        
        # Adjust row/column weights for responsiveness
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
            self.expression += "**0.5"
        elif button_text == "^":
            self.expression += "**"
        elif button_text in ["sin", "cos", "tan", "arcsin", "arccos", "arctan"]:
            self.expression += f"Calculator.{button_text}("
        else:
            self.expression += button_text
        
        self.update_display()

    def key_press(self, event):
        """Handles keyboard input"""
        key = event.char
        if key in "0123456789+-*/().":
            self.expression += key
        elif key == "\r":  # Enter key
            self.calculate_result()
        elif key == "\x08":  # Backspace key
            self.expression = self.expression[:-1]
        self.update_display()

    def calculate_result(self):
        """Evaluates the expression using the Calculator module"""
        try:
            result = eval(self.expression, {"Calculator": Calculator, "math": __import__("math")})
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Calculation")
            self.expression = ""
        self.update_display()

    def update_display(self):
        """Updates the display with the current expression"""
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

def run_gui():
    """Runs the calculator GUI"""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
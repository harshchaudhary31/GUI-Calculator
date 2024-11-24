import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math Error", "Division by zero is not allowed.")
        else:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x300")

# Input fields
tk.Label(window, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack(pady=5)

tk.Label(window, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Buttons for operations
tk.Button(window, text="Add", command=add).pack(pady=5)
tk.Button(window, text="Subtract", command=subtract).pack(pady=5)
tk.Button(window, text="Multiply", command=multiply).pack(pady=5)
tk.Button(window, text="Divide", command=divide).pack(pady=5)

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)

# Run the main loop
window.mainloop()

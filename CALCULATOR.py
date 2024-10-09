import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            result = "Invalid operation"
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))
root = tk.Tk()
root.title("Simple Calculator")
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)
label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)
operation_var = tk.StringVar(value='+')
label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)
radio_add = tk.Radiobutton(root, text="Add (+)", variable=operation_var, value='+')
radio_add.grid(row=3, column=0, padx=10, pady=5)
radio_subtract = tk.Radiobutton(root, text="Subtract (-)", variable=operation_var, value='-')
radio_subtract.grid(row=3, column=1, padx=10, pady=5)
radio_multiply = tk.Radiobutton(root, text="Multiply (*)", variable=operation_var, value='*')
radio_multiply.grid(row=4, column=0, padx=10, pady=5)
radio_divide = tk.Radiobutton(root, text="Divide (/)", variable=operation_var, value='/')
radio_divide.grid(row=4, column=1, padx=10, pady=5)
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()




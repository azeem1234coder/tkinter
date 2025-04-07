import tkinter as tk
from tkinter import messagebox

# Function to calculate the product
def calculate_product():
    try:
        # Get the values from the entry fields
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Calculate the product
        product = num1 * num2
        
        # Display the result
        result_label.config(text=f"Product: {product}")
    except ValueError:
        # Display error message if input is not valid
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Product Calculator")

# Create and place labels, entries, and button
label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Product: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

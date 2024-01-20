# Create app to check credit card numbers for validity

import tkinter as tk
from tkinter import ttk

def luhn_check(card_number):
    # Remove spaces and non-numeric characters from the input
    card_number = ''.join(filter(str.isdigit, card_number))

    # Check if the input is empty or contains non-numeric characters
    if not card_number:
        return False

    # Reverse the card number and convert it to a list of integers
    card_digits = [int(digit) for digit in card_number[::-1]]

    # Double every second digit, starting from the right
    for i in range(1, len(card_digits), 2):
        card_digits[i] *= 2
        if card_digits[i] > 9:
            card_digits[i] -= 9

    # Calculate the sum of all digits
    total = sum(card_digits)

    # Check if the total is divisible by 10
    return total % 10 == 0

def check_card():
    card_number = card_entry.get()
    if luhn_check(card_number):
        result_label.config(text="Valid credit card number.", fg="white")
    else:
        result_label.config(text="Invalid credit card number.", fg="red")

def mask_card_number(event):
    # Get the card number from the entry field
    card_number = card_entry.get()
    
    # Mask all but the last four digits
    masked_card = '*' * (len(card_number) - 4) + card_number[-4:]
    
    # Set the masked card number in the entry field
    card_entry.delete(0, tk.END)
    card_entry.insert(0, masked_card)

# Create the main window
root = tk.Tk()
root.title("Luhn Algorithm Checker")
root.geometry("400x200") 

# Set a modern color scheme
root.configure(bg="#1E88E5")  # Background color

# Create and configure a custom style for buttons
button_style = ttk.Style()
button_style.configure("Modern.TButton", foreground="black", background="#2196F3", font=("Roboto", 12), borderwidth=0)

# Create and configure widgets
instruction_label = tk.Label(root, text="Enter a credit card number:", bg="#1E88E5", fg="white", font=("Roboto", 14))
card_entry = tk.Entry(root, font=("Roboto", 12))
check_button = ttk.Button(root, text="Check", command=check_card, style="Modern.TButton")
result_label = tk.Label(root, text="", fg="green", bg="#1E88E5", font=("Roboto", 12))

# Bind the mask_card_number function to the entry field's focus out event
card_entry.bind("<FocusOut>", mask_card_number)

# Arrange widgets using the grid layout
instruction_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
card_entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
check_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
result_label.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

# Start the GUI main loop
root.mainloop()


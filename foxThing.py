import tkinter as tk
import random

# Initialize the pool of letters
letter_pool = ['f'] * 5 + ['o'] * 6 + ['x'] * 5
random.shuffle(letter_pool)  # Shuffle to randomize the selection

# Function to update button text when clicked
def on_button_click(btn):
    if letter_pool:  # Ensure the pool is not empty
        letter = letter_pool.pop()
        btn.config(text=letter)

# Create the main window
root = tk.Tk()
root.title("4x4 Grid of Letters")

# Create a 4x4 grid of buttons
buttons = []
for row in range(4):
    button_row = []
    for col in range(4):
        btn = tk.Button(root, text='', width=10, height=5)
        btn.config(command=lambda b=btn: on_button_click(b))  # Assign command after button creation
        btn.grid(row=row, column=col)
        button_row.append(btn)
    buttons.append(button_row)

# Start the tkinter main loop
root.mainloop()

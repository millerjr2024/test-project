import tkinter as tk
import random

# Function to determine the winner
def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("300x250")

# Title label
title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Arial', 12))
title_label.pack(pady=10)

# Buttons
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=('Arial', 10), fg="blue")
result_label.pack(pady=20)

# Start GUI
root.mainloop()

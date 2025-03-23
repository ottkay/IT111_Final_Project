import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x500")
root.configure(bg='white')

# Load images
rock_img = ImageTk.PhotoImage(Image.open("images/rock.png").resize((150, 150)))
paper_img = ImageTk.PhotoImage(Image.open("images/paper.png").resize((150, 150)))
scissors_img = ImageTk.PhotoImage(Image.open("images/scissors.png").resize((150, 150)))

# Grid layout with padding for consistency
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Labels
title_label = Label(root, text="Your Choice", font=("Helvetica", 18, "bold"), bg='white')
title_label.grid(row=0, column=1, pady=10)

# Player and computer images centered
player_img = Label(root, image=rock_img, bg='white')
player_img.grid(row=1, column=0, padx=30)

computer_img = Label(root, image=paper_img, bg='white')
computer_img.grid(row=1, column=2, padx=30)

# Result label
result_label = Label(root, text="Computer: ", font=("Helvetica", 14), bg='white')
result_label.grid(row=2, column=1, pady=20)

# Function to update images and show result
def play(choice):
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    # Update player image
    player_img.config(image=rock_img if choice == "rock" else 
                             paper_img if choice == "paper" else scissors_img)

    # Update computer image
    computer_img.config(image=rock_img if computer == "rock" else 
                                paper_img if computer == "paper" else scissors_img)

    # Determine the winner
    result = "Tie!"
    if (choice == "rock" and computer == "scissors") or \
       (choice == "paper" and computer == "rock") or \
       (choice == "scissors" and computer == "paper"):
        result = "You Win!"
    elif choice != computer:
        result = "You Lose!"

    result_label.config(text=f"Computer: {computer.capitalize()} | {result}")

# Buttons with better spacing and sizing
btn_rock = Button(root, text="Rock", command=lambda: play("rock"), width=12, height=2)
btn_rock.grid(row=3, column=0, pady=20, padx=10)

btn_paper = Button(root, text="Paper", command=lambda: play("paper"), width=12, height=2)
btn_paper.grid(row=3, column=1, pady=20, padx=10)

btn_scissors = Button(root, text="Scissors", command=lambda: play("scissors"), width=12, height=2)
btn_scissors.grid(row=3, column=2, pady=20, padx=10)

# Run GUI loop
root.mainloop()

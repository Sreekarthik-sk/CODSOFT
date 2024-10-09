import tkinter as tk
from tkinter import messagebox
import random
def play(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    label_computer_choice.config(text=f"Computer's Choice: {computer_choice}")
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        global user_score
        user_score += 1
    else:
        result = "Computer wins!"
        global computer_score
        computer_score += 1
    label_result.config(text=result)
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score, computer_score = 0, 0
    label_result.config(text="")
    label_computer_choice.config(text="")
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
app = tk.Tk()
app.title("Rock, Paper, Scissors Game")
user_score = 0
computer_score = 0
label_instruction = tk.Label(app, text="Choose Rock, Paper, or Scissors:")
label_instruction.pack(pady=10)
button_rock = tk.Button(app, text="Rock", width=15, command=lambda: play("Rock"))
button_rock.pack(pady=5)
button_paper = tk.Button(app, text="Paper", width=15, command=lambda: play("Paper"))
button_paper.pack(pady=5)
button_scissors = tk.Button(app, text="Scissors", width=15, command=lambda: play("Scissors"))
button_scissors.pack(pady=5)
label_computer_choice = tk.Label(app, text="")
label_computer_choice.pack(pady=10)
label_result = tk.Label(app, text="", font=("Arial", 16))
label_result.pack(pady=10)
label_score = tk.Label(app, text=f"Score - You: {user_score} | Computer: {computer_score}", font=("Arial", 14))
label_score.pack(pady=10)
button_reset = tk.Button(app, text="Reset Game", width=15, command=reset_game)
button_reset.pack(pady=20)
app.mainloop()

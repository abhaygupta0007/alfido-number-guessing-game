import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Guessing Game")
        self.geometry("400x350")
        self.config(bg="#282c34")
        self.resizable(False, False)

        self.random_number = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        # Heading
        heading = tk.Label(self, text="Guess a Number (1-100)", font=("Helvetica", 18, "bold"), bg="#282c34", fg="white")
        heading.pack(pady=20)

        # Entry
        self.entry = tk.Entry(self, font=("Helvetica", 16), justify="center", width=10)
        self.entry.pack(pady=10)

        # Submit Button
        submit_btn = tk.Button(self, text="Submit Guess", font=("Helvetica", 14), bg="#61afef", fg="white", command=self.check_guess)
        submit_btn.pack(pady=10)

        # Result
        self.result_label = tk.Label(self, text="", font=("Helvetica", 14), bg="#282c34", fg="#e5c07b")
        self.result_label.pack(pady=10)

        # Attempts
        self.attempts_label = tk.Label(self, text="Attempts: 0", font=("Helvetica", 12), bg="#282c34", fg="white")
        self.attempts_label.pack(pady=5)

        # Reset Button
        reset_btn = tk.Button(self, text="Play Again", font=("Helvetica", 12), bg="#98c379", fg="white", command=self.reset_game)
        reset_btn.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            messagebox.showwarning("Invalid input", "Please enter a number between 1 and 100.")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.random_number:
            self.result_label.config(text="Too Low! Try again.")
        elif guess > self.random_number:
            self.result_label.config(text="Too High! Try again.")
        else:
            self.result_label.config(text=f"Correct! The number was {self.random_number}.")
            messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.attempts_label.config(text="Attempts: 0")

if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()

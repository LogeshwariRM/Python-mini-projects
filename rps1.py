import random
import tkinter as tk
from tkinter import messagebox

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
CHOICES = [ROCK, PAPER, SCISSORS]

class RPSGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.player1_score = 0
        self.player2_score = 0
        self.winning_score = 5

        self.root = tk.Tk()
        self.root.title("Rock-Paper-Scissors")
        self.root.configure(bg="white")
        self.root.geometry("500x600")

        self.button_bg = "lightblue"
        self.button_font = ("Helvetica", 14)

        tk.Label(self.root, text="Welcome to Rock, Paper, Scissors!", bg="white", font=("Helvetica", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Play Rock-Paper-Scissors (Single Player)", command=self.play_single_player, bg=self.button_bg, font=self.button_font, height=2, width=40).pack(pady=10)
        tk.Button(self.root, text="Play Rock-Paper-Scissors (Multiplayer)", command=self.play_multi_player, bg=self.button_bg, font=self.button_font, height=2, width=40).pack(pady=10)
        tk.Button(self.root, text="View Scores", command=self.view_scores, bg=self.button_bg, font=self.button_font, height=2, width=40).pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.root.quit, bg=self.button_bg, font=self.button_font, height=2, width=40).pack(pady=10)

    def get_computer_choice(self):
        return random.choice(CHOICES)

    def determine_winner(self, user_choice, opponent_choice):
        if user_choice == opponent_choice:
            return "tie"
        elif (user_choice == ROCK and opponent_choice == SCISSORS) or \
             (user_choice == PAPER and opponent_choice == ROCK) or \
             (user_choice == SCISSORS and opponent_choice == PAPER):
            return "user"
        else:
            return "opponent"

    def play_single_player(self):
        self.player_score = 0
        self.computer_score = 0
        self.show_choices("single")

    def play_multi_player(self):
        self.player1_score = 0
        self.player2_score = 0
        self.show_choices("multi")

    def view_scores(self):
        messagebox.showinfo("Scores", f"Single Player Scores:\nPlayer score: {self.player_score} | Computer score: {self.computer_score}\n\nMultiplayer Scores:\nPlayer 1 score: {self.player1_score} | Player 2 score: {self.player2_score}")

    def show_choices(self, mode):
        self.choice_window = tk.Toplevel(self.root)
        self.choice_window.title("Make your choice")
        self.choice_window.configure(bg="white")
        self.choice_window.geometry("400x300")

        tk.Label(self.choice_window, text="Choose Rock, Paper, or Scissors:", bg="white", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.choice_window, text="Rock", command=lambda: self.make_choice("rock", mode), bg=self.button_bg, font=self.button_font, height=2, width=15).pack(pady=5)
        tk.Button(self.choice_window, text="Paper", command=lambda: self.make_choice("paper", mode), bg=self.button_bg, font=self.button_font, height=2, width=15).pack(pady=5)
        tk.Button(self.choice_window, text="Scissors", command=lambda: self.make_choice("scissors", mode), bg=self.button_bg, font=self.button_font, height=2, width=15).pack(pady=5)

    def make_choice(self, user_choice, mode):
        if mode == "single":
            computer_choice = self.get_computer_choice()
            result = self.determine_winner(user_choice, computer_choice)
            if result == "tie":
                messagebox.showinfo("Result", f"It's a tie! You both chose {user_choice}.")
            elif result == "user":
                messagebox.showinfo("Result", f"You win! You chose {user_choice} and the computer chose {computer_choice}.")
                self.player_score += 1
            else:
                messagebox.showinfo("Result", f"Computer wins! You chose {user_choice} and the computer chose {computer_choice}.")
                self.computer_score += 1

            if self.player_score == self.winning_score:
                messagebox.showinfo("Game Over", "Congratulations! You won the game!")
            elif self.computer_score == self.winning_score:
                messagebox.showinfo("Game Over", "Sorry, the computer won the game.")
            else:
                self.choice_window.destroy()
                self.show_choices("single")

        elif mode == "multi":
            if hasattr(self, 'player1_choice'):
                player2_choice = user_choice
                result = self.determine_winner(self.player1_choice, player2_choice)
                if result == "tie":
                    messagebox.showinfo("Result", f"It's a tie! You both chose {self.player1_choice}.")
                elif result == "user":
                    messagebox.showinfo("Result", f"Player 1 wins! Player 1 chose {self.player1_choice} and Player 2 chose {player2_choice}.")
                    self.player1_score += 1
                else:
                    messagebox.showinfo("Result", f"Player 2 wins! Player 1 chose {self.player1_choice} and Player 2 chose {player2_choice}.")
                    self.player2_score += 1

                delattr(self, 'player1_choice')

                if self.player1_score == self.winning_score:
                    messagebox.showinfo("Game Over", "Congratulations! Player 1 won the game!")
                elif self.player2_score == self.winning_score:
                    messagebox.showinfo("Game Over", "Congratulations! Player 2 won the game.")
                else:
                    self.choice_window.destroy()
                    self.show_choices("multi")

            else:
                self.player1_choice = user_choice
                self.choice_window.destroy()
                self.show_choices("multi")

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = RPSGame()
    game.start()

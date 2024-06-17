import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman Game")
        self.geometry("500x600")
        self.hangman_stages = self.create_hangman_stages()
        self.word_to_guess = "elephant"
        self.display_word = ["_" for _ in self.word_to_guess]
        self.wrong_guesses = 0
        self.max_guesses = len(self.hangman_stages)
        self.create_widgets()

        # Load and set the icon
        icon_image = PhotoImage(file="hangman.png")  # Ensure the hangman.png file is in the same directory as the script
        self.iconphoto(False, icon_image)
    
    def create_hangman_stages(self):
        return [
            r'''
             +------++      
             |      ||
                    ||
                    ||
                    ||
                    ||
          ==============
             ''',
            r'''
             +------++      
             |      ||
             O      ||
                    ||
                    ||
                    ||
          ==============
             ''',
            r'''
             +------++      
             |      ||
             O      ||
             |      ||
                    ||
                    ||
          ==============
             ''',
            r'''
             +------++      
             |      ||
             O      ||
            /|      ||
                    ||
                    ||
          ==============
             ''',
            r'''
             +------++      
             |      ||
             O      ||
            /|\     ||
                    ||
                    ||
          ==============
             ''',
            r'''
             +------++      
             |      ||
             O      ||
            /|\     ||
            /       ||
                    ||
          ==============
             ''',
            r'''
             +------++      
             |      ||
             O      ||
            /|\     ||
            / \     ||
                    ||
          ==============
             '''
        ]
    
    def create_widgets(self):
        self.hangman_label = tk.Label(self, text=self.hangman_stages[0], font=('Courier', 12), justify='left')
        self.hangman_label.pack(pady=20)

        self.word_label = tk.Label(self, text=" ".join(self.display_word), font=('Helvetica', 24))
        self.word_label.pack(pady=20)

        self.entry_label = tk.Label(self, text="Guess a letter:", font=('Helvetica', 14))
        self.entry_label.pack()

        self.letter_entry = tk.Entry(self, font=('Helvetica', 14))
        self.letter_entry.pack()
        self.letter_entry.bind("<Return>", self.check_letter)

        self.guesses_label = tk.Label(self, text=f"Chances left: {self.max_guesses - self.wrong_guesses}", font=('Helvetica', 14))
        self.guesses_label.pack(pady=20)
    
    def check_letter(self, event):
        letter = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)

        if letter in self.word_to_guess:
            for index, char in enumerate(self.word_to_guess):
                if letter == char:
                    self.display_word[index] = letter
            self.word_label.config(text=" ".join(self.display_word))
            
            if "_" not in self.display_word:
                messagebox.showinfo("Hangman", f"Congratulations! You've guessed the word: {''.join(self.display_word)}")
                self.reset_game()
        else:
            self.wrong_guesses += 1
            self.guesses_label.config(text=f"Chances left: {self.max_guesses - self.wrong_guesses}")
            if self.wrong_guesses < self.max_guesses:
                self.hangman_label.config(text=self.hangman_stages[self.wrong_guesses])

            if self.wrong_guesses == self.max_guesses:
                messagebox.showinfo("Hangman", f"Sorry, you've run out of chances. The word was: {self.word_to_guess}")
                self.reset_game()
    
    def reset_game(self):
        self.wrong_guesses = 0
        self.word_to_guess = "ambitious"
        self.display_word = ["_" for _ in self.word_to_guess]
        self.hangman_label.config(text=self.hangman_stages[0])
        self.word_label.config(text=" ".join(self.display_word))
        self.guesses_label.config(text=f"Chances left: {self.max_guesses - self.wrong_guesses}")

if __name__ == "__main__":
    game = HangmanGame()
    game.mainloop()

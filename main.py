from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, win_logo, welcome_logo


class Hangman:
    def __init__(self):
        self.chosen_word = random.choice(word_list)
        self.word_length = len(self.chosen_word)
        self.lives = 6
        self.end_of_game = False
        self.display = ["_" for _ in range(self.word_length)]
        self.wrong_guesses = set()
        self.guess_char = ""

    def display_welcome(self):
        print(welcome_logo)
        print("\nTo  win, guess the word before the person is hung.\n")

    def check_repeatition(self):
        if self.guess_char in self.wrong_guesses:
            print(stages[self.lives])
            print(f"{' '.join(self.display)}")
            print(
                f"You've already guessed the letter {self.guess_char}, pick another letter."
            )
            return True

        self.wrong_guesses.add(self.guess_char)
        return False

    def good_guess(self):
        print(stages[self.lives])
        for position, value in enumerate(self.chosen_word):
            if value == self.guess_char:
                self.display[position] = self.guess_char
        print(f"{' '.join(self.display)}")

        if "_" not in self.display:
            self.end_of_game = True
            print("\nGenius! you won the game.")
            print(win_logo)

    def wrong_guess(self):
        self.lives -= 1
        print(f"{' '.join(self.display)}")
        print(stages[self.lives])
        print(f"'{self.guess_char}' is not the word")

        if self.lives == 0:
            self.end_of_game = True
            print("The man has been hung, you lose!")
            print(f"\n The word was '{self.chosen_word}'")

    def play(self):
        self.display_welcome()
        while not self.end_of_game:
            self.guess_char = input("Guess a char:").lower()
            clear()
            if not self.check_repeatition():
                if self.guess_char in self.chosen_word:
                    self.good_guess()
                else:
                    self.wrong_guess()


if __name__ == "__main__":
    game = Hangman()
    game.play()

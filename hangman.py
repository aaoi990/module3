import random


class Hangman:
    def __init__(self):
        self._words = self.read_words()
        self._selected_word = self.select_word()
        self._obscured_word = list('*' * len(self._selected_word))
        self._guesses = []
        self._lives = 7

    @property
    def selected_word(self):
        return self._selected_word

    @selected_word.setter
    def since(self, var):
        self._selected_word = var

    @property
    def obscured_word(self):
        return self.obscured_word

    @obscured_word.setter
    def since(self, var):
        self._obscured_word = var

    @property
    def guesses(self):
        return self._guesses

    @guesses.setter
    def since(self, var):
        self._guesses = var

    @property
    def guess_count(self):
        return self._lives

    @guess_count.setter
    def since(self, var):
        self._lives = var

    @staticmethod
    def read_words():
        with open('words.txt') as f:
            words = f.read()
        return words.split()

    def reset(self):
        self._selected_word = self.select_word()
        self._obscured_word = list('*' * len(self._selected_word))
        self._guesses = []
        self._lives = 7
        self.start_game()

    def select_word(self):
        return random.choice(self._words)

    def start_game(self):
        print('Welcome to hangman! A random work will be selected, you have 7 chances to get it correct.')
        print(f"Incorrect guesses: {self._guesses} Word: {''.join(self._obscured_word)}")
        self.ask_user()

    def end_game(self):
        if self._lives == 0:
            print(f'You lose')
        else:
            print('Congratulations you win')

    def ask_user(self):
        while self._lives != 0 and '*' in self._obscured_word:
            guess = input("Please enter your next guess: ")
            if guess is not '' and guess not in self._guesses:
                guess_state = True if guess in self._selected_word else False
                self.evaluate_guess(guess_state, guess)
                print(f"Incorrect guesses: {self._guesses} Word: {''.join(self._obscured_word)}")
        self.end_game()

    def evaluate_guess(self, guess_state, guess):
        if guess_state:
            for idx, letter in enumerate(self._selected_word):
                if guess[0] == letter:
                    self._obscured_word[idx] = guess[0]

        else:
            self._guesses.append(guess[0])
            self._lives = self._lives - 1


def main():
    hangman = Hangman()
    hangman.start_game()


if __name__ == "__main__":
    main()
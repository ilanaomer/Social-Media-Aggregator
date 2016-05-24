class Hangman(object):
    def __init__(self, secret_word, tries):
        self.secret_word = secret_word
        self.tries = tries
        self.lst_secret_word = ['?'] * len(self.secret_word)
        self.tries = tries

    def status(self):
        return "".join(self.lst_secret_word)

    def guess(self, guess_letter):
        self.tries -= 1 # TODO: only if letter not found
        if self.tries < 0:
            raise GameOver(self.secret_word)

        for i, c in enumerate(self.secret_word):
            if c == guess_letter:
                self.lst_secret_word[i] = c
        return self.secret_word.count(guess_letter)

    def game_won(self):
        return "".join(self.lst_secret_word) == self.secret_word

class GameOver(Exception):
    def __init__(self, word):
        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, 'The word was "{}"'.format(word))



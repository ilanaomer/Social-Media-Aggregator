from hangman import Hangman

game = Hangman("Hello", 10)
print(game.status())
# ?????
print(game.guess('H'))
# 1
print(game.status())
# H????
print(game.guess('e'))
# 1
print(game.status())
# He???
print(game.guess('H'))
# -1
print(game.status())
# He???
print(game.guess('l'))
# 2
print(game.status())
# Hell?
print(game.guess('o'))
# 1
print(game.status())
# Hello

# game.guess('a')
# game.guess('a')
# game.guess('a')
# game.guess('a')
# game.guess('a')
# game.guess('a')
# game.guess('a')
# game.guess('a')
# game.guess('a')
# game.guess('a')
# game.guess('a')
# hangman.GameOver: The word was "Hello"
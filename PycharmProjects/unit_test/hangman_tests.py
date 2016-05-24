import unittest
from hangman import Hangman, GameOver


class TestHangman(unittest.TestCase):
    def setUp(self):
        self.game = Hangman("Hello", 10)

    def test_status(self):
        self.assertEqual(self.game.status(), '?????')

    def test_guess(self):
        self.assertEqual(self.game.guess('H'), 1)
        self.assertEqual(self.game.status(), 'H????')

    def test_bad_guess(self):
        self.assertEqual(self.game.guess('h'), 0)
        self.assertEqual(self.game.status(), '?????')

    def test_good_guess(self):
        self.assertEqual(self.game.guess('e'), 1)
        self.assertEqual(self.game.status(), '?e???')

    def test_multiple_guess(self):
        self.assertEqual(self.game.guess('l'), 2)
        self.assertEqual(self.game.status(), '??ll?')

    def test_game_over(self):
        with self.assertRaises(GameOver):
            for i in range(self.game.tries + 1):
                self.game.guess('a')

    def test_game_won(self):
        self.game.guess('H')
        self.game.guess('e')
        self.game.guess('l')
        self.game.guess('l')
        self.game.guess('o')
        self.assertEqual(self.game.game_won(), True)

if __name__ == '__main__':
    unittest.main()

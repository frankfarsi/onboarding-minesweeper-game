import unittest
from minesweeper.src.Game import Game


class EmptyBoardOnStartTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_board_is_empty_on_start(self):
        self.given_the_game_is_not_started()
        self.when_the_game_is_started()
        self.then_the_board_is_empty()

    def given_the_game_is_not_started(self):
        game = Game()

    def when_the_game_is_started(self):
        self.game.start()

    def then_the_board_is_empty(self):
        assert self.game.board.isEmpty() == True


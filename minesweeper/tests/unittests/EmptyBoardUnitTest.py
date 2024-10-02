import unittest

from minesweeper.src.Game import Game
from minesweeper.tests.unittests.BoardUtilies import BoardUtilities


class EmptyBoardUnitTest(unittest.TestCase):


    def setUp(self):
        self.game = Game()

    def test_game_is_not_started_on_creation(self):
        assert self.game.isRunning == False

    def test_when_game_is_started_it_is_running(self):
        self.game.start()
        assert self.game.isRunning == True

    def test_board_is_empty_on_start(self):
        assert self.game.board.cells == BoardUtilities.create_empty_board()
        assert self.game.board.isEmpty() == True;


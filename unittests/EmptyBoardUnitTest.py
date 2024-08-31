import unittest

from Cell import Cell
from Game import Game
from State import State


class EmptyBoardUnitTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_is_not_started_on_creation(self):
        assert self.game.isRunning == False

    def test_when_game_is_started_it_is_running(self):
        self.game.start()
        assert self.game.isRunning == True

    def test_board_is_empty_on_start(self):
        expected_cells = []
        for i in range(9):
            row= []
            for j in range(9):
                row.append(Cell(State.EMPTY))
            expected_cells.append(row)

        print(self.game.board.cells)

        assert self.game.board.cells == expected_cells
        assert self.game.board.isEmpty() == True;
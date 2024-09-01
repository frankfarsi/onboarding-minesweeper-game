from pdb import find_function
from typing import List

from minesweeper.src.Cell import Cell
from minesweeper.src.State import State


class Board:
    def __init__(self):
        self.isBoardEmpty = False
        self.cells = []
        self.initialize_cells()

    def initialize_cells(self)-> None:
        for i in range(9):
            row = []
            for j in range(9):
                row.append(Cell(State.EMPTY))
            self.cells.append(row)

        self.isBoardEmpty = True

    def isEmpty(self) -> bool:
        return self.isBoardEmpty
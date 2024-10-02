from typing import List

from minesweeper.src.Cell import Cell
from minesweeper.src.State import State


class BoardUtilities:
    @staticmethod
    def create_empty_board() -> List[List[Cell]]:
        expected_cells = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(Cell(State.EMPTY))
            expected_cells.append(row)
        return expected_cells
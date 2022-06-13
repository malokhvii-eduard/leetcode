"""`36. Valid Sudoku <https://leetcode.com/problems/valid-sudoku/>`_

>>> Solution().isValidSudoku([
...     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
...     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
...     [".", "9", "8", ".", ".", ".", ".", "6", "."],
...     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
...     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
...     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
...     [".", "6", ".", ".", ".", ".", "2", "8", "."],
...     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
...     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
... ])
True

>>> Solution().isValidSudoku([
...     ["8", "3", ".", ".", "7", ".", ".", ".", "8"],
...     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
...     [".", "9", "8", ".", ".", ".", ".", "6", "."],
...     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
...     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
...     ["7", ".", ".", "1", "2", ".", ".", ".", "6"],
...     [".", "6", ".", ".", ".", ".", "2", "8", "."],
...     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
...     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
... ])
False
"""

from typing import List, Set


class Solution:
    BOX_SIZE = 3
    BOARD_SIZE = 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Determines if a Sudoku board is valid."""
        n, b = self.BOARD_SIZE, self.BOX_SIZE

        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue

                try:
                    self.addCell(rows[i], cell)
                    self.addCell(columns[j], cell)
                    self.addCell(boxes[((i // b) * b) + j // b], cell)
                except ValueError:
                    return False

        return True

    def addCell(self, cells: Set[str], cell: str):
        """Adds cell into cells without repetition, otherwise raises ValueError."""
        if cell in cells:
            raise ValueError("Duplicate number detected in cells!")

        cells.add(cell)

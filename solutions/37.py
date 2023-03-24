"""`37. Sudoku Solver <https://leetcode.com/problems/sudoku-solver/>`_

>>> board1 = [
...     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
...     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
...     [".", "9", "8", ".", ".", ".", ".", "6", "."],
...     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
...     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
...     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
...     [".", "6", ".", ".", ".", ".", "2", "8", "."],
...     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
...     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
... ]
>>> Solution().solveSudoku(board1)
>>> board1
[['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', \
'4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', \
'1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', \
'9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', \
'8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]

>>> board2 = [
...     ["7", "9", ".", ".", ".", ".", "6", ".", "5"],
...     ["6", "2", ".", "3", "5", "9", ".", "7", "4"],
...     ["5", "4", "3", "1", "6", ".", "9", ".", "2"],
...     ["9", "1", "4", ".", ".", "8", ".", ".", "."],
...     [".", ".", ".", "5", "3", ".", "8", ".", "9"],
...     [".", "8", ".", "2", "9", "1", ".", "6", "7"],
...     [".", ".", ".", ".", "4", "6", ".", "9", "."],
...     ["4", "3", ".", "8", ".", ".", ".", "2", "6"],
...     [".", "6", ".", ".", "2", "3", "5", "4", "."],
... ]
>>> Solution().solveSudoku(board2)
>>> board2
[['7', '9', '1', '4', '8', '2', '6', '3', '5'], ['6', '2', '8', '3', '5', '9', '1', \
'7', '4'], ['5', '4', '3', '1', '6', '7', '9', '8', '2'], ['9', '1', '4', '6', '7', \
'8', '2', '5', '3'], ['2', '7', '6', '5', '3', '4', '8', '1', '9'], ['3', '8', '5', \
'2', '9', '1', '4', '6', '7'], ['8', '5', '2', '7', '4', '6', '3', '9', '1'], ['4', \
'3', '9', '8', '1', '5', '7', '2', '6'], ['1', '6', '7', '9', '2', '3', '5', '4', '8']]
"""

from itertools import product
from typing import Dict, Generator, List, Set, Tuple


Cell = Tuple[int, int, int]
Key = Tuple[str, Tuple[int, int]]
Y = Dict[Cell, List[Key]]
X = Dict[Key, Set[Cell]]


class Solution:
    BOX_SIZE = 3
    BOARD_SIZE = 9

    def solveSudoku(self, board: List[List[str]]):
        """Solve a Sudoku puzzle using `Knuth's Algorithm X
        <https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X>`_. See also an
        `explanation of the algorithm <https://habr.com/ru/post/462411/>`_.
        """
        n, b = self.BOARD_SIZE, self.BOX_SIZE

        # ("rc", row, column): there is a number at the intersection of row and column.
        # ("rn", row, num): the row contains the number.
        # ("cn", column, num): the column contains the number.
        # ("bn", box, num): the box contains the number.

        # Fill rows.
        y: Y = {}
        for row, column, num in product(range(n), range(n), range(1, n + 1)):
            box = (row // b) * b + (column // b)
            y[(row, column, num)] = [
                ("rc", (row, column)),
                ("rn", (row, num)),
                ("cn", (column, num)),
                ("bn", (box, num)),
            ]

        # Fill columns.
        x: X = {
            k: set()
            for k in (
                [("rc", rc) for rc in product(range(n), range(n))]
                + [("rn", rn) for rn in product(range(n), range(1, n + 1))]
                + [("cn", cn) for cn in product(range(n), range(1, n + 1))]
                + [("bn", bn) for bn in product(range(n), range(1, n + 1))]
            )
        }
        for i, row in y.items():
            for j in row:
                x[j].add(i)

        # Enter those numbers that are already filled in.
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != ".":
                    # Removes all incompatible elements from the matrix.
                    self.select(x, y, (i, j, int(num)))

        # Find cover (solution).
        for solution in self.solve(x, y, []):
            for row, column, num in solution:
                board[row][column] = str(num) if num != 0 else "."

    def solve(self, x: X, y: Y, cover: List[Cell]) -> Generator[List[Cell], None, None]:
        """Find cover (solution) a Sudoku puzzle."""
        if not x:
            yield cover
        else:
            # Look for a column with the minimum number of elements.
            column = min(x, key=lambda c: len(x[c]))
            for cell in list(x[column]):
                cover.append(cell)
                # Remove overlapping subsets and elements contained in the subset.
                cells = self.select(x, y, cell)

                # If a non-empty solution is found - done, exits.
                yield from self.solve(x, y, cover)

                self.deselect(x, y, cell, cells)
                cover.pop()

    def select(self, x: X, y: Y, cell: Cell) -> List[Set[Cell]]:
        """Extract all intersecting columns."""
        cells = []
        for j in y[cell]:
            # Remove all intersecting rows from all remaining columns.
            for i in x[j]:
                for k in y[i]:
                    if k != j:
                        x[k].remove(i)

            # Remove the current column from the table to the buffer.
            cells.append(x.pop(j))

        return cells

    def deselect(self, x: X, y: Y, cell: Cell, cells: List[Set[Cell]]):
        """Delete columns from the first intersection with cell to the last, we need
        to restore in reverse order.
        """
        for j in reversed(y[cell]):
            x[j] = cells.pop()
            for i in x[j]:
                for k in y[i]:
                    if k != j:
                        x[k].add(i)

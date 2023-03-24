"""`2194. Cells in a Range on an Excel Sheet <https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/>`_

>>> list(Solution().cellsInRange('K1:L2'))
['K1', 'K2', 'L1', 'L2']

>>> list(Solution().cellsInRange('A1:F1'))
['A1', 'B1', 'C1', 'D1', 'E1', 'F1']
"""

from typing import Generator


class Solution:
    def cellsInRange(self, s: str) -> Generator[str, None, None]:
        """Return the list of cells in a spreadsheet range."""
        col1, row1, col2, row2 = s[0], s[1], s[3], s[4]
        for col in range(ord(col1), ord(col2) + 1):
            for row in range(int(row1), int(row2) + 1):
                yield f"{chr(col)}{row}"

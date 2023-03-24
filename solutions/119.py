"""`119. Pascal's Triangle II <https://leetcode.com/problems/pascals-triangle-ii/>`_

>>> Solution().getRow(3)
[1, 3, 3, 1]

>>> Solution().getRow(0)
[1]

>>> Solution().getRow(1)
[1, 1]

>>> Solution().getRow(4)
[1, 4, 6, 4, 1]
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """Return the row of the Pascal's triangle."""
        n = rowIndex + 1
        if n == 1:
            return [1]

        previous = [1, 1]
        for row in range(2, n):
            current = [1]

            for i, j in zip(range(len(previous) - 1), range(1, len(previous))):
                current.append(previous[i] + previous[j])

            current.append(1)
            previous = current

        return previous

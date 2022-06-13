"""`118. Pascal's Triangle <https://leetcode.com/problems/pascals-triangle/>`_

>>> Solution().generate(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

>>> Solution().generate(1)
[[1]]

>>> Solution().generate(2)
[[1], [1, 1]]
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """Returns the first numRows of Pascal's triangle."""
        if numRows == 1:
            return [[1]]

        triangle = [[1], [1, 1]]
        for row in range(2, numRows):
            previous, current = triangle[row - 1], [1]

            for i, j in zip(range(len(previous) - 1), range(1, len(previous))):
                current.append(previous[i] + previous[j])

            current.append(1)
            triangle.append(current)

        return triangle

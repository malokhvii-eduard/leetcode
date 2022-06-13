"""`48. Rotate Image <https://leetcode.com/problems/rotate-image/>`_

>>> matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
>>> Solution().rotate(matrix)
>>> matrix
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]

>>> matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
>>> Solution().rotate(matrix)
>>> matrix
[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

>>> matrix = [
...     [1, 2, 3, 4, 5],
...     [6, 7, 8, 9, 10],
...     [11, 12, 13, 14, 15],
...     [16, 17, 18, 19, 20],
...     [21, 22, 23, 24, 25]
... ]
>>> Solution().rotate(matrix)
>>> matrix
[[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]):
        """Rotates the image by 90 degrees (clockwise)."""
        n = len(matrix)
        w = n // 2 if n % 2 == 0 else n // 2 + 1

        for i in range(n // 2):  # depth
            for j in range(w):  # width
                # a > 7  4  1 < b
                #     8  5  2
                # d > 9  6  3 < c
                a = matrix[i][j]
                # d -> a
                matrix[i][j] = matrix[n - j - 1][i]
                # c -> d
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                # b -> c
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                # a -> b
                matrix[j][n - i - 1] = a

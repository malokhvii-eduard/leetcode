"""`1486. XOR Operation in an Array <https://leetcode.com/problems/xor-operation-in-an-array/>`_

>>> Solution().xorOperation(5, 0)
8

>>> Solution().xorOperation(4, 3)
8

>>> Solution().xorOperation(1, 7)
7
"""

from functools import reduce
from operator import xor


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """Return the bitwise XOR of all elements of nums."""
        if n == 1:
            return start

        return reduce(xor, range(start, start + n * 2, 2))

"""`191. Number of 1 Bits <https://leetcode.com/problems/number-of-1-bits/>`_

>>> Solution().hammingWeight(0b00000000000000000000000000001011)
3

>>> Solution().hammingWeight(0b00000000000000000000000010000000)
1

>>> Solution().hammingWeight(0b11111111111111111111111111111101)
31
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """Returns the number of '1' bits."""
        counter = 0
        while n:
            n &= n - 1
            counter += 1

        return counter

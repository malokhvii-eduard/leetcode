"""`342. Power of Four <https://leetcode.com/problems/power-of-four/>`_

>>> Solution().isPowerOfFour(16)
True

>>> Solution().isPowerOfFour(5)
False

>>> Solution().isPowerOfFour(1)
True
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """Return true if it is a power of four, and false otherwise."""
        if n < 1:
            return False

        while n % 4 == 0:
            n /= 4

        return n == 1

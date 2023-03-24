"""`231. Power of Two <https://leetcode.com/problems/power-of-two/>`_

>>> Solution().isPowerOfTwo(1)
True

>>> Solution().isPowerOfTwo(16)
True

>>> Solution().isPowerOfTwo(3)
False
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """Return true if it is a power of two, and false otherwise."""
        if n < 1:
            return False

        while n % 2 == 0:
            n /= 2

        return n == 1

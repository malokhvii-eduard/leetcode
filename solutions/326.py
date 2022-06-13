"""`326. Power of Three <https://leetcode.com/problems/power-of-three/>`_

>>> Solution().isPowerOfThree(27)
True

>>> Solution().isPowerOfThree(0)
False

>>> Solution().isPowerOfThree(9)
True
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """Returns true if it is a power of three, and false otherwise."""
        if n < 1:
            return False

        while n % 3 == 0:
            n /= 3

        return n == 1

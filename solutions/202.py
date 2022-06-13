"""`202. Happy Number <https://leetcode.com/problems/happy-number/>`_

>>> Solution().isHappy(19)
True

>>> Solution().isHappy(932)
True

>>> Solution().isHappy(2)
False

>>> Solution().isHappy(4)
False

>>> Solution().isHappy(999)
False
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """Determines if a number n is happy."""
        squares_sum, duplicates = n, set()
        while squares_sum != 1 and squares_sum not in duplicates:
            duplicates.add(squares_sum)
            squares_sum = sum(map(lambda x: x**2, map(int, str(squares_sum))))

        return squares_sum == 1

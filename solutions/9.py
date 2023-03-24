"""`9. Palindrome Number <https://leetcode.com/problems/palindrome-number/>`_

>>> Solution().isPalindrome(121)
True

>>> Solution().isPalindrome(1001)
True

>>> Solution().isPalindrome(0)
True

>>> Solution().isPalindrome(-121)
False

>>> Solution().isPalindrome(10)
False
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Return true if x is palindrome integer."""
        if x < 0:
            return False

        digits = list(map(int, str(x)))
        for i in range(len(digits) // 2):
            if digits[i] != digits[len(digits) - 1 - i]:
                return False

        return True

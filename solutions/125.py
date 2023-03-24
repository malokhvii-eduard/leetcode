"""`125. Valid Palindrome <https://leetcode.com/problems/valid-palindrome/>`_

>>> Solution().isPalindrome("A man, a plan, a canal: Panama")
True

>>> Solution().isPalindrome("race a car")
False

>>> Solution().isPalindrome(" ")
True
"""


import string


class Solution:
    PRINTABLE = str.maketrans("", "", string.whitespace + string.punctuation)

    def isPalindrome(self, s: str) -> bool:
        """Return true if it is a palindrome, or false otherwise."""
        s = s.translate(self.PRINTABLE).lower()
        return s == s[::-1]

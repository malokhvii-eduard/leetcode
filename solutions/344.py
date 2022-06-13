"""`344. Reverse String <https://leetcode.com/problems/reverse-string/>`_

>>> s = ["h", "e", "l", "l", "o"]
>>> Solution().reverseString(s)
>>> s
['o', 'l', 'l', 'e', 'h']

>>> s = ["H", "a", "n", "n", "a", "h"]
>>> Solution().reverseString(s)
>>> s
['h', 'a', 'n', 'n', 'a', 'H']
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Reverses a string in-place."""
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

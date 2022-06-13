"""`242. Valid Anagram <https://leetcode.com/problems/valid-anagram/>`_

>>> Solution().isAnagram("anagram", "nagaram")
True

>>> Solution().isAnagram("rat", "car")
False
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Returns true if t is an anagram of s, and false otherwise."""
        return Counter(s) == Counter(t)

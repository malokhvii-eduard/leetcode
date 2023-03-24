"""`387. First Unique Character in a String <https://leetcode.com/problems/first-unique-character-in-a-string/>`_

>>> Solution().firstUniqChar("leetcode")
0

>>> Solution().firstUniqChar("loveleetcode")
2

>>> Solution().firstUniqChar("aabb")
-1
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Return index of first non-repeating character."""
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i

        return -1

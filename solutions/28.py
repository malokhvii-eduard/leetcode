"""`28. Implement strStr() <https://leetcode.com/problems/implement-strstr/>`_

>>> Solution().strStr("hello", "ll")
2

>>> Solution().strStr("aaaaa", "bba")
-1

>>> Solution().strStr("", "")
0

>>> Solution().strStr("a", "a")
0

>>> Solution().strStr("mississippi", "issipi")
-1

>>> Solution().strStr("mississippi", "issip")
4
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of needle in haystack."""
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i : m + i] == needle:
                return i

        return -1

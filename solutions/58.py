"""`58. Length of Last Word <https://leetcode.com/problems/length-of-last-word/>`_

>>> Solution().lengthOfLastWord("Hello World")
5

>>> Solution().lengthOfLastWord("   fly me   to   the moon  ")
4

>>> Solution().lengthOfLastWord("luffy is still joyboy")
6
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Return the length of the last word in the string."""
        s = s.rstrip()
        # fmt: off
        return len(s[s.rfind(" ") + 1:])
        # fmt: on

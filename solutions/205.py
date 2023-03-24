"""`205. Isomorphic Strings <https://leetcode.com/problems/isomorphic-strings/>`_

>>> Solution().isIsomorphic("egg", "add")
True

>>> Solution().isIsomorphic("foo", "bar")
False

>>> Solution().isIsomorphic("paper", "title")
True

>>> Solution().isIsomorphic("badc", "baba")
False
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Determine if two strings are isomorphic."""
        sm, tm = {}, {}
        for cs, ct in zip(s, t):
            if cs not in sm:
                sm[cs] = ct

            if ct not in tm:
                tm[ct] = cs

            if sm[cs] != ct or tm[ct] != cs:
                return False

        return True

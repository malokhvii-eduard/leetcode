"""`345. Reverse Vowels of a String <https://leetcode.com/problems/reverse-vowels-of-a-string/>`_

>>> Solution().reverseVowels("hello")
'holle'

>>> Solution().reverseVowels("leetcode")
'leotcede'
"""


class Solution:
    VOWELS = frozenset("aAeEiIoOuU")

    def reverseVowels(self, s: str) -> str:
        """Reverse only all the vowels in the string."""
        reversed_s = list(s)

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] not in self.VOWELS:
                i += 1
                continue

            if s[j] not in self.VOWELS:
                j -= 1
                continue

            reversed_s[i], reversed_s[j] = reversed_s[j], reversed_s[i]
            i += 1
            j -= 1

        return "".join(reversed_s)

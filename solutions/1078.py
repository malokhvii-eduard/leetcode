"""`1078. Occurrences After Bigram <https://leetcode.com/problems/occurrences-after-bigram/>`_

>>> Solution().findOcurrences("alice is a good girl she is a good student", "a", "good")
['girl', 'student']

>>> Solution().findOcurrences("we will we will rock you", "we", "will")
['we', 'rock']
"""

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        """Return an array of all the words third for each occurrence of 'first second third'."""
        words = text.split(" ")

        occurrences = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                occurrences.append(words[i + 2])

        return occurrences

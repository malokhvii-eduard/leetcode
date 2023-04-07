"""`1128. Number of Equivalent Domino Pairs <https://leetcode.com/problems/number-of-equivalent-domino-pairs/>`_

>>> Solution().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]])
1

>>> Solution().numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]])
3
"""

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
        and dominoes[i] is equivalent to dominoes[j].
        """
        counter = {}
        for a, b in dominoes:
            if (a, b) in counter:
                counter[(a, b)] += 1
            elif (b, a) in counter:
                counter[(b, a)] += 1
            else:
                counter[(a, b)] = 1

        equivalent_pairs = 0
        for count in counter.values():
            equivalent_pairs += count * (count - 1) / 2

        return int(equivalent_pairs)

"""`2404. Most Frequent Even Element <https://leetcode.com/problems/most-frequent-even-element/>`_

>>> Solution().mostFrequentEven([0, 1, 2, 2, 4, 4, 1])
2

>>> Solution().mostFrequentEven([4, 4, 4, 9, 2, 4])
4

>>> Solution().mostFrequentEven([29, 47, 21, 41, 13, 37, 25, 7])
-1

>>> Solution().mostFrequentEven([8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290])
3346
"""

from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        """Return the most frequent even element."""
        even_nums = list(filter(lambda x: x % 2 == 0, nums))
        if not even_nums:
            return -1

        most_frequent, _ = Counter(sorted(even_nums)).most_common()[0]
        return most_frequent

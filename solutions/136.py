"""`136. Single Number <https://leetcode.com/problems/single-number/>`_

>>> Solution().singleNumber([2, 2, 1])
1

>>> Solution().singleNumber([4, 1, 2, 1, 2])
4

>>> Solution().singleNumber([1])
1
"""

from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Find single number."""
        counter = Counter(nums)
        for num in counter.keys():
            if counter[num] == 1:
                return num

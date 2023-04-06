"""`229. Majority Element II <https://leetcode.com/problems/majority-element-ii/>`_

>>> Solution().majorityElement([3, 2, 3])
[3]

>>> Solution().majorityElement([1])
[1]

>>> Solution().majorityElement([1, 2])
[1, 2]

>>> Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2])
[1, 2]
"""

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """Return the majority elements."""
        majority_elements = []

        majority_count = len(nums) // 3
        for num, count in Counter(sorted(nums)).most_common():
            if count > majority_count:
                majority_elements.append(num)
            else:
                break

        return majority_elements

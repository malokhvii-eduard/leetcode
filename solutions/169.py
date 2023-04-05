"""`169. Majority Element <https://leetcode.com/problems/majority-element/>`_

>>> Solution().majorityElement([3, 2, 3])
3

>>> Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
2
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Return the majority element. `Boyer–Moore majority vote algorithm
        <https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm>`_.
        """
        count, majority_element = 0, 0
        for num in nums:
            if count == 0:
                majority_element = num

            if majority_element == num:
                count += 1
            else:
                count -= 1

        return majority_element

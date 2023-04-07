"""`414. Third Maximum Number <https://leetcode.com/problems/third-maximum-number/>`_

>>> Solution().thirdMax([3, 2, 1])
1

>>> Solution().thirdMax([1 ,2])
2

>>> Solution().thirdMax([2, 2, 3, 1])
1
"""

from math import inf
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Return the third distinct maximum number in this array. If the third
        maximum does not exist, return the maximum number.
        """
        max1 = max2 = max3 = -inf
        for num in nums:
            if num in (max1, max2, max3):
                continue

            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num

        return max3 if max3 != -inf else max1

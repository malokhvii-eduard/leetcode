"""`350. Intersection of Two Arrays II <https://leetcode.com/problems/intersection-of-two-arrays-ii/>`_

>>> Solution().intersect([1, 2, 2, 1], [2, 2])
[2, 2]

>>> Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])
[9, 4]

>>> Solution().intersect([1, 2, 2, 1], [2])
[2]

>>> Solution().intersect([1, 2], [1, 1])
[1]
"""

from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Return an intersection of two arrays."""
        if len(nums1) >= len(nums2):
            longer, shorter = nums1, nums2
        else:
            longer, shorter = nums2, nums1

        counter = dict(Counter(shorter))

        answer = []
        for num in longer:
            if num in counter:
                counter[num] -= 1
                answer.append(num)

                if counter[num] <= 0:
                    counter.pop(num)

        return answer

"""`349. Intersection of Two Arrays <https://leetcode.com/problems/intersection-of-two-arrays/>`_

>>> Solution().intersection([1, 2, 2, 1], [2, 2])
[2]

>>> Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])
[4, 9]
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Returns an unique intersection of two arrays."""
        nums2, unique = frozenset(nums2), set()

        answer = []
        for num in nums1:
            if num in nums2 and num not in unique:
                unique.add(num)
                answer.append(num)

        return answer

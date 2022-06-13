"""`278. First Bad Version <https://leetcode.com/problems/first-bad-version/>`_"""


def isBadVersion(version: int) -> bool:
    """The isBadVersion API is already defined, this is a stub."""
    ...


class Solution(object):
    def firstBadVersion(self, n: int) -> int:
        """Detects first bad version. Uses binary search."""
        left, right = 1, n
        while left <= right:
            middle = left + (right - left) // 2
            if isBadVersion(middle):
                right = middle - 1
            else:
                left = middle + 1

        return left

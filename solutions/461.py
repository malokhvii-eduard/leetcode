"""`461. Hamming Distance <https://leetcode.com/problems/hamming-distance/>`_

>>> Solution().hammingDistance(1, 4)
2

>>> Solution().hammingDistance(3, 1)
1
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """`The Hamming distance <https://en.wikipedia.org/wiki/Hamming_distance>`_
        between two integers is the number of positions at which the corresponding bits
        are different."""
        distance = 0

        # The ^ operators sets to 1 only the bits that are different
        z = x ^ y
        while z:
            # We then count the bit set to 1 using the Peter Wegner way
            z = z & (z - 1)  # Set to zero val's lowest-order 1
            distance += 1

        return distance

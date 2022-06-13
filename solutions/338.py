"""`338. Counting Bits <https://leetcode.com/problems/counting-bits/>`_

>>> Solution().countBits(2)
[0, 1, 1]

>>> Solution().countBits(5)
[0, 1, 1, 2, 1, 2]

>>> Solution().countBits(0)
[0]
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """Returns an array with a number of 1's in the binary representation of each
        number in the range [0, n]."""
        return list(map(lambda x: x.bit_count(), range(n + 1)))

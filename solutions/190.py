"""`190. Reverse Bits <https://leetcode.com/problems/reverse-bits/>`_

>>> Solution().reverseBits(43261596)
964176192

>>> Solution().reverseBits(4294967293)
3221225471
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        """Reverses bits of an unsigned integer."""
        answer = 0
        for i in range(32):
            answer = answer << 1 | ((n >> i) & 1)

        return answer

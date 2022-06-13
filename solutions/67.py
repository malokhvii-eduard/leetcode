"""`67. Add Binary <https://leetcode.com/problems/add-binary/>`_

>>> Solution().addBinary("11", "1")
'100'

>>> Solution().addBinary("1010", "1011")
'10101'

>>> Solution().addBinary("111", "0")
'111'

>>> Solution().addBinary("0", "0")
'0'

>>> Solution().addBinary("1111", "1111")
'11110'
"""

from collections import deque
from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Return a + b as a binary string."""
        answer = deque()

        carry = 0
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            result = int(x) + int(y) + carry
            carry = result // 2
            result %= 2
            answer.appendleft(str(result))

        if carry:
            answer.appendleft("1")

        return "".join(answer)

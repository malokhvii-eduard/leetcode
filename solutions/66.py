"""`66. Plus One <https://leetcode.com/problems/plus-one/>`_

>>> Solution().plusOne([1, 2, 3])
[1, 2, 4]

>>> Solution().plusOne([4, 3, 2, 1])
[4, 3, 2, 2]

>>> Solution().plusOne([9])
[1, 0]

>>> Solution().plusOne([9, 9, 9, 9])
[1, 0, 0, 0, 0]
"""

from collections import deque
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Increments the large integer by one and return the resulting
        array of digits."""
        answer = deque()

        carry = 1
        while digits and carry != 0:
            result = digits.pop() + carry
            carry = result // 10
            result %= 10
            answer.appendleft(result)

        if digits:
            answer.extendleft(reversed(digits))

        if carry:
            answer.appendleft(1)

        return list(answer)

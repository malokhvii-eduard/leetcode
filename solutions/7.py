"""`7. Reverse Integer <https://leetcode.com/problems/reverse-integer/>`_

>>> Solution().reverse(123)
321

>>> Solution().reverse(-123)
-321

>>> Solution().reverse(120)
21

>>> Solution().reverse(1463847412)
2147483641

>>> Solution().reverse(-2147447412)
-2147447412

>>> Solution().reverse(2147483647)
0

>>> Solution().reverse(-2147483648)
0
"""


class Solution:
    def reverse(self, x: int) -> int:
        """Returns x with its digits reversed"""
        r = str(abs(x))
        r = r.strip()
        r = r[::-1]

        answer = int(r)
        if answer > 2**31 - 1 or answer < -(2**31):
            return 0

        return -answer if x < 0 else answer

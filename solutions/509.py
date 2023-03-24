"""`509. Fibonacci Number <https://leetcode.com/problems/fibonacci-number/>`_

>>> Solution().fib(2)
1

>>> Solution().fib(3)
2

>>> Solution().fib(4)
3

>>> Solution().fib(30)
832040
"""


class Solution:
    def fib(self, n: int) -> int:
        """Calculate F(N), where F(0) = 0, F(1) = 1, F(n) = F(n - 1) + F(n - 2)."""
        x, y = 0, 1
        for _ in range(n):
            x, y = y, x + y

        return x

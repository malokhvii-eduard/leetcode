"""`412. Fizz Buzz <https://leetcode.com/problems/fizz-buzz/>`_

>>> list(Solution().fizzBuzz(3))
['1', '2', 'Fizz']

>>> list(Solution().fizzBuzz(5))
['1', '2', 'Fizz', '4', 'Buzz']

>>> list(Solution().fizzBuzz(15))
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', \
'14', 'FizzBuzz']
"""

from typing import Generator


class Solution:
    def fizzBuzz(self, n: int) -> Generator[str, None, None]:
        """Returns a Fizz Buzz string sequence."""
        for x in range(1, n + 1):
            if x % 15 == 0:
                yield "FizzBuzz"
            elif x % 5 == 0:
                yield "Buzz"
            elif x % 3 == 0:
                yield "Fizz"
            else:
                yield str(x)

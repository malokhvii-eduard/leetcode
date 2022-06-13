"""`204. Count Primes <https://leetcode.com/problems/count-primes/>`_

>>> Solution().countPrimes(10)
4

>>> Solution().countPrimes(0)
0

>>> Solution().countPrimes(1)
0
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        """Returns number of prime numbers that are strictly less than n. Uses the
        Sieve of Eratosthenes."""
        is_prime = [True] * n

        i = 2
        while i * i < n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i

            i += 1

        counter = 0
        for i in range(2, n):
            if is_prime[i]:
                counter += 1

        return counter

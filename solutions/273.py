"""`273. Integer to English Words <https://leetcode.com/problems/integer-to-english-words/>`_

>>> Solution().numberToWords(0)
'Zero'

>>> Solution().numberToWords(123)
'One Hundred Twenty Three'

>>> Solution().numberToWords(12345)
'Twelve Thousand Three Hundred Forty Five'

>>> Solution().numberToWords(1234567)
'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'

>>> Solution().numberToWords(1234567891)
'One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One'

>>> Solution().numberToWords(1234567891234)
'One Trillion Two Hundred Thirty Four Billion Five Hundred Sixty Seven Million Eight Hundred Ninety One Thousand Two Hundred Thirty Four'

>>> Solution().numberToWords(1234567891234567)
'One Quadrillion Two Hundred Thirty Four Trillion Five Hundred Sixty Seven Billion Eight Hundred Ninety One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'

>>> Solution().numberToWords(2**31 - 1)
'Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven'
"""

from typing import Generator


class Solution:
    TEN = 10
    ONE_HUNDRED = 100
    ONE_THOUSAND = 1000
    ONE_MILLION = 1000000
    ONE_BILLION = 1000000000
    ONE_TRILLION = 1000000000000
    ONE_QUADRILLION = 1000000000000000
    MAX = 9007199254740992

    LESS_THAN_TWENTY = (
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    )

    TENTHS_LESS_THAN_HUNDRED = (
        "Zero",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    )

    def numberToWords(self, num: int) -> str:
        """Converts a non-negative integer to its English words representation."""
        return " ".join(self.generate(num))

    def generate(
        self, num: int, _is_first_num: bool = True
    ) -> Generator[str, None, None]:
        """Generates a sequence of English words that represent a non-negative integer."""
        if num == 0:
            if _is_first_num:
                yield "Zero"

            return

        remainder = None

        if num < 20:
            remainder = 0
            yield self.LESS_THAN_TWENTY[num]
        elif num < self.ONE_HUNDRED:
            quotient, remainder = divmod(num, self.TEN)
            yield self.TENTHS_LESS_THAN_HUNDRED[quotient]

            if remainder != 0:
                yield self.LESS_THAN_TWENTY[remainder]
                remainder = 0
        elif num < self.ONE_THOUSAND:
            quotient, remainder = divmod(num, self.ONE_HUNDRED)
            yield from self.generate(quotient, False)
            yield "Hundred"
        elif num < self.ONE_MILLION:
            quotient, remainder = divmod(num, self.ONE_THOUSAND)
            yield from self.generate(quotient, False)
            yield "Thousand"
        elif num < self.ONE_BILLION:
            quotient, remainder = divmod(num, self.ONE_MILLION)
            yield from self.generate(quotient, False)
            yield "Million"
        elif num < self.ONE_TRILLION:
            quotient, remainder = divmod(num, self.ONE_BILLION)
            yield from self.generate(quotient, False)
            yield "Billion"
        elif num < self.ONE_QUADRILLION:
            quotient, remainder = divmod(num, self.ONE_TRILLION)
            yield from self.generate(quotient, False)
            yield "Trillion"
        elif num <= self.MAX:
            quotient, remainder = divmod(num, self.ONE_QUADRILLION)
            yield from self.generate(quotient, False)
            yield "Quadrillion"

        yield from self.generate(remainder, False)

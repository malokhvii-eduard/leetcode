"""`12. Integer to Roman <https://leetcode.com/problems/integer-to-roman/>`_

>>> Solution().intToRoman(3)
'III'

>>> Solution().intToRoman(58)
'LVIII'

>>> Solution().intToRoman(100)
'C'

>>> Solution().intToRoman(1994)
'MCMXCIV'
"""


class Solution:
    ROMAN = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def intToRoman(self, num: int) -> str:
        """Converts integer to roman numeral."""
        symbols = []

        for base in self.ROMAN.keys():
            while num >= base:
                symbols.append(self.ROMAN[base])
                num -= base

            if num == 0:
                break

        return "".join(symbols)

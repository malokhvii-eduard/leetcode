"""`13. Roman to Integer <https://leetcode.com/problems/roman-to-integer/>`_

>>> Solution().romanToInt("III")
3

>>> Solution().romanToInt("LVIII")
58

>>> Solution().romanToInt("MCMXCIV")
1994
"""


class Solution:
    ROMAN = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        """Converts roman numeral to an integer."""
        number = 0
        for i in range(len(s) - 1):
            current_symbol, next_symbol = self.ROMAN[s[i]], self.ROMAN[s[i + 1]]
            if current_symbol >= next_symbol:
                number += current_symbol
            else:
                number -= current_symbol

        number += self.ROMAN[s[len(s) - 1]]
        return abs(number)

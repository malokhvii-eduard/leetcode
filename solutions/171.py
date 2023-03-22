"""`171. Excel Sheet Column Number <https://leetcode.com/problems/excel-sheet-column-number/>`_

>>> Solution().titleToNumber('A')
1

>>> Solution().titleToNumber('AB')
28

>>> Solution().titleToNumber('ZY')
701

>>> Solution().titleToNumber('FXSHRXW')
2147483647
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """Converts column title from an Excel sheet, to corresponding
        number."""
        columnNumber = 0
        for letter in map(ord, columnTitle):
            columnNumber *= 26
            columnNumber += letter - 65 + 1

        return columnNumber

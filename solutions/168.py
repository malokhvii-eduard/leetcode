"""`168. Excel Sheet Column Title <https://leetcode.com/problems/excel-sheet-column-title/>`_

>>> Solution().convertToTitle(1)
'A'

>>> Solution().convertToTitle(28)
'AB'

>>> Solution().convertToTitle(701)
'ZY'

>>> Solution().convertToTitle(2**31 - 1)
'FXSHRXW'
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """Convert integer column number to corresponding column title as it
        appears in an Excel sheet.
        """
        letters = []
        while columnNumber > 0:
            quotient, remainder = divmod(columnNumber - 1, 26)

            letters.append(chr(remainder + 65))

            columnNumber = quotient

        return "".join(reversed(letters))

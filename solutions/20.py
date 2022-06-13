"""`20. Valid Parentheses <https://leetcode.com/problems/valid-parentheses/>`_

>>> Solution().isValid("()")
True

>>> Solution().isValid("()[]{}")
True

>>> Solution().isValid("(]")
False

>>> Solution().isValid("{ { ( { } ) } }")
True

>>> Solution().isValid("{ { (      ) } }")
True

>>> Solution().isValid("{ {          } }")
True

>>> Solution().isValid("{                }")
True

>>> Solution().isValid("{{{{")
False

>>> Solution().isValid("{{}}}}}")
False
"""


from typing import Iterable, Tuple


class Solution:
    PARENTHESES = {"(": ")", "[": "]", "{": "}"}
    OPEN_PARENTHESES = set(PARENTHESES.keys())
    CLOSE_PARENTHESES = set(PARENTHESES.values())

    def isValid(self, s: str) -> bool:
        """Determines if the input string with parentheses is valid."""
        open_parentheses = []
        for parenthesis, is_open in self.onlyParentheses(s):
            if is_open:
                open_parentheses.append(parenthesis)
            else:
                if not open_parentheses:
                    return False

                open_parenthesis = open_parentheses.pop()
                if parenthesis != self.PARENTHESES[open_parenthesis]:
                    return False

        return not open_parentheses

    def onlyParentheses(self, s: str) -> Iterable[Tuple[str, bool]]:
        """Returns only parentheses from string."""
        for c in s:
            if c in self.OPEN_PARENTHESES:
                yield c, True
            elif c in self.CLOSE_PARENTHESES:
                yield c, False

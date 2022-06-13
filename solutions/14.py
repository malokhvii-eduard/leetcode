"""`14. Longest Common Prefix <https://leetcode.com/problems/longest-common-prefix/>`_

>>> Solution().longestCommonPrefix(["flower", "flow", "flight"])
'fl'

>>> Solution().longestCommonPrefix(["dog", "racecar", "car"])
''
"""

from collections import OrderedDict
from itertools import takewhile
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Finds the longest common prefix string amongst an array of strings."""
        counter = OrderedDict()
        for s in strs:
            for i, c in enumerate(s):
                counter[(c, i)] = counter.get((c, i), 0) + 1

        prefix = [k[0] for k in takewhile(lambda x: counter[x] == len(strs), counter)]
        return "".join(prefix)

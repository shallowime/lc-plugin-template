#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30201
#
# [76] 最小覆盖子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        left, right = 0, 0
        vaild = 0
        start, length = 0, float('inf')
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    vaild += 1
            while vaild == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        vaild -= 1
                    window[d] -= 1
        return s[start:start + length] if length != float('inf') else ''
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.minWindow("ADOBECODEBANC", "ABC"))


#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#


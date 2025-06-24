#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=30201
#
# [567] 字符串的排列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = {}, {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        left, right = 0, 0
        vaild = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    vaild += 1
            while vaild == len(need):
                if right - left == len(s1):
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        vaild -= 1
                    window[d] -= 1
        return False
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.checkInclusion("ab", "eidbaooo"))


#
# @lcpr case=start
# "eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "eidboaoo"\n
# @lcpr case=end

#


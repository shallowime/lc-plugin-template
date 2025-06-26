#
# @lc app=leetcode.cn id=424 lang=python3
# @lcpr version=30201
#
# [424] 替换后的最长重复字符
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        windowCharCount = [0] * 26

        windowMaxCharCount = 0
        res = 0
        while right < len(s):
            c = ord(s[right]) - ord('A')
            windowCharCount[c] += 1
            windowMaxCharCount = max(windowMaxCharCount, windowCharCount[c])
            right += 1
            while right - left - windowMaxCharCount > k:
                d = ord(s[left]) - ord('A')
                windowCharCount[d] -= 1
                left += 1
            res = max(res, right - left)
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.characterReplacement("ABAB", 2))
    print(solution.characterReplacement("AABABBA", 1))


#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#


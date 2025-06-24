#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30201
#
# [125] 验证回文串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sb = []
        for c in s:
            if c.isalnum():
                sb.append(c.lower())
        s = ''.join(sb)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False        
            left += 1
            right -= 1
        return True
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#


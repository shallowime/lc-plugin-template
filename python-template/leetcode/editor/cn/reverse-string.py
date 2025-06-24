#
# @lc app=leetcode.cn id=344 lang=python3
# @lcpr version=30201
#
# [344] 反转字符串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    print(s)


#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#


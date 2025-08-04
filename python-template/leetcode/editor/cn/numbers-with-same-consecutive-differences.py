#
# @lc app=leetcode.cn id=967 lang=python3
# @lcpr version=30201
#
# [967] 连续差相同的数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        self.track = 0
        self.digit = 0

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.backtrack(n, k)
        return self.res
    
    def backtrack(self, n: int, k: int) -> None:
        if self.digit == n:
            self.res.append(self.track)
            return
        
        for i in range(10):
            if self.digit == 0 and i == 0:
                continue
            if self.digit > 0 and abs(self.track % 10 - i) != k:
                continue
            self.digit += 1
            self.track = self.track * 10 + i
            self.backtrack(n, k)
            self.digit -= 1
            self.track = self.track // 10
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.numsSameConsecDiff(3, 7))


#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 2\n1\n
# @lcpr case=end

# @lcpr case=start
# 2\n0\n
# @lcpr case=end

# @lcpr case=start
# 2\n2\n
# @lcpr case=end

#


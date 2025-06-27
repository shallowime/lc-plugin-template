#
# @lc app=leetcode.cn id=96 lang=python3
# @lcpr version=30201
#
# [96] 不同的二叉搜索树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:

    def __init__(self):
        self.memo = {}

    def numTrees(self, n: int) -> int:
        self.memo = [[0] * (n + 1) for _ in range(n + 1)]
        return self.count(1, n)

    def count(self, lo:int, hi:int) -> int:
        if lo > hi:
            return 1
        
        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]
        
        res = 0
        for mid in range(lo, hi + 1):
            left = self.count(lo, mid - 1)
            right = self.count(mid + 1, hi)
            res += left * right
        
        self.memo[lo][hi] = res
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


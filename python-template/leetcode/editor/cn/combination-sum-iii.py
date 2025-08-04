#
# @lc app=leetcode.cn id=216 lang=python3
# @lcpr version=30201
#
# [216] 组合总和 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.track = []
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k <= 0 or n <= 0:
            return self.res
        self.backtrack(k, n, 1, 0)
        return self.res
    
    def backtrack(self, k: int, n: int, start: int, sum: int):
        if sum > n:
            return
        if sum == n and len(self.track) == k:
            self.res.append(self.track.copy())
            return
        for i in range(start, 10):
            self.track.append(i)
            sum += i
            self.backtrack(k, n, i + 1, sum)
            self.track.pop()
            sum -= i

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(3, 7))



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n9\n
# @lcpr case=end

# @lcpr case=start
# 4\n1\n
# @lcpr case=end

#


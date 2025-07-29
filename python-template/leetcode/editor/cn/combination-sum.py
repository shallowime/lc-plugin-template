#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30201
#
# [39] 组合总和
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

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.res
        self.backtrack(candidates, 0, target, 0)
        return self.res
    
    def backtrack(self, candidates: List[int], start: int, target: int, sum: int):
        if sum > target:
            return
        if sum == target:
            self.res.append(self.track.copy())
            return
        for i in range(start, len(candidates)):
            self.track.append(candidates[i])
            sum += candidates[i]
            self.backtrack(candidates, i, target, sum)
            self.track.pop()
            sum -= candidates[i]

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#


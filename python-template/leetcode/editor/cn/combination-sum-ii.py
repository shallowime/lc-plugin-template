#
# @lc app=leetcode.cn id=40 lang=python3
# @lcpr version=30201
#
# [40] 组合总和 II
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
    

    #可重不可复选，先排序，然后加一条剪枝逻辑
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.res
        candidates.sort()
        self.backtrack(candidates, 0, target, 0)
        return self.res
    
    def backtrack(self, candidates: List[int], start: int, target: int, sum: int):
        if sum > target:
            return
        if sum == target:
            self.res.append(self.track.copy())
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            self.track.append(candidates[i])
            sum += candidates[i]
            self.backtrack(candidates, i + 1, target, sum)
            self.track.pop()
            sum -= candidates[i]

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))



#
# @lcpr case=start
# [10,1,2,7,6,1,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2,5,2,1,2]\n5\n
# @lcpr case=end

#


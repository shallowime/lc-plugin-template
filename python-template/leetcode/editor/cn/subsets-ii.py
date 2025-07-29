#
# @lc app=leetcode.cn id=90 lang=python3
# @lcpr version=30201
#
# [90] 子集 II
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
        self.track = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], start: int):
        self.res.append(self.track.copy())

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([1, 2, 2]))



#
# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


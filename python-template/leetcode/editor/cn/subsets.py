#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30201
#
# [78] 子集
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

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], start: int):
        self.res.append(self.track.copy())

        for i in range(start, len(nums)):
            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


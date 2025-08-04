#
# @lc app=leetcode.cn id=47 lang=python3
# @lcpr version=30201
#
# [47] 全排列 II
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

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        track = []
        used = [False] * len(nums)
        nums.sort()
        self.backtrack(nums, track, used)
        return self.res
    
    def backtrack(self, nums: List[int], track: List[int], used: List[bool]):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            track.append(nums[i])
            used[i] = True
            self.backtrack(nums, track, used)
            track.pop()
            used[i] = False

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#


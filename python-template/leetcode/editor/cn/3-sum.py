#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30201
#
# [15] 三数之和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.nSumTarget(nums, 3, 0, 0)
    
    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        sz = len(nums)
        res = []

        if n < 2 or sz < n:
            return res
        
        if n == 2:
            lo, hi = start, sz - 1
            while lo < hi:
                sum_val = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if sum_val < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif sum_val > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            for i in range(start, sz):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0,1,1]))
    print(solution.threeSum([0,0,0]))



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#


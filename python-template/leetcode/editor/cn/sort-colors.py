#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30201
#
# [75] 颜色分类
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        p = 0
        while p <= p2:
            if nums[p] == 0:
                self.swap(nums, p0, p)
                p0 += 1
            elif nums[p] == 2:
                self.swap(nums, p2, p)
                p2 -= 1
            elif nums[p] == 1:
                p += 1
            
            if p < p0:
                p = p0

    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    print(nums)


#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#


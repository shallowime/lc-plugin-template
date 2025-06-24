#
# @lc app=leetcode.cn id=977 lang=python3
# @lcpr version=30201
#
# [977] 有序数组的平方
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        p = n - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                res[p] = nums[left] ** 2
                left += 1
            else:
                res[p] = nums[right] ** 2
                right -= 1
            p -= 1
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [-4, -1, 0, 3, 10]
    print(solution.sortedSquares(nums))


#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#


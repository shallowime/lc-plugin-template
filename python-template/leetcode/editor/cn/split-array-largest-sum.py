#
# @lc app=leetcode.cn id=410 lang=python3
# @lcpr version=30201
#
# [410] 分割数组的最大值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.f(nums, mid) <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def f(self, nums: List[int], x: int) -> int:
        days = 0
        i = 0
        while i < len(nums):
            cap = x
            while i < len(nums):
                if nums[i] > cap:
                    break
                else:
                    cap -= nums[i]
                    i += 1
            days += 1
        return days
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.splitArray([7, 2, 5, 10, 8], 2))
    print(solution.splitArray([1, 2, 3, 4, 5], 2))
    print(solution.splitArray([1, 4, 4], 3))


#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,4,4]\n3\n
# @lcpr case=end

#


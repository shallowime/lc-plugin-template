#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30201
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchLeft(nums, target), self.searchRight(nums, target)]

    def searchLeft(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def searchRight(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        return right
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(solution.searchRange([], 0))


#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#


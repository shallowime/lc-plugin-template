#
# @lc app=leetcode.cn id=704 lang=python3
# @lcpr version=30201
#
# [704] 二分查找
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))
    print(solution.search([-1, 0, 3, 5, 9, 12], 2))


#
# @lcpr case=start
# [-1,0,3,5,9,12]\n9\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,3,5,9,12]\n2\n
# @lcpr case=end

#


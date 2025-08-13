#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30201
#
# [42] 接雨水
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        res = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(solution.trap([4,2,0,3,2,5]))



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#


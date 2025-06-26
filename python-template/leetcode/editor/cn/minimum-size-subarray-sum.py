#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30201
#
# [209] 长度最小的子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sum = 0
        res = float('inf')
        while right < len(nums):
            sum += nums[right]
            right += 1
            while sum >= target:
                res = min(res, right - left)
                sum -= nums[left]
                left += 1
        return res if res != float('inf') else 0
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(solution.minSubArrayLen(4, [1, 4, 4]))
    print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))


#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#


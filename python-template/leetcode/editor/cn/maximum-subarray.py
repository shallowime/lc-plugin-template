#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30201
#
# [53] 最大子数组和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(solution.maxSubArray([1]))
    print(solution.maxSubArray([5,4,-1,7,8]))


#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#


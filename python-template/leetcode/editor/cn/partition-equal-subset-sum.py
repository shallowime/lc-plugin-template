#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30201
#
# [416] 分割等和子集
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        n = len(nums)
        target = sum_nums // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j >= nums[i - 1]:
                    # 背包容量充足：
                    # 装入或者不装入背包
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    # 背包容量不足：
                    # 不装入背包
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.canPartition([1,5,11,5]))
    print(solution.canPartition([1,2,3,5]))


#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#


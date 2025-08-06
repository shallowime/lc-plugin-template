#
# @lc app=leetcode.cn id=509 lang=python3
# @lcpr version=30201
#
# [509] 斐波那契数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        # 分别代表 dp[i - 1] 和 dp[i - 2]
        dp_i_1 = 1
        dp_i_2 = 0
        for _ in range(2, n + 1):
            # dp[i] = dp[i - 1] + dp[i - 2];
            dp_i = dp_i_1 + dp_i_2
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(3))



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#


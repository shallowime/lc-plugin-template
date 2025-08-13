#
# @lc app=leetcode.cn id=263 lang=python3
# @lcpr version=30201
#
# [263] 丑数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(6))
    print(solution.isUgly(1))
    print(solution.isUgly(14))



#
# @lcpr case=start
# 6\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 14\n
# @lcpr case=end

#


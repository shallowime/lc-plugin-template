#
# @lc app=leetcode.cn id=292 lang=python3
# @lcpr version=30201
#
# [292] Nim 游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.canWinNim(4))
    print(solution.canWinNim(1))
    print(solution.canWinNim(2))



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#


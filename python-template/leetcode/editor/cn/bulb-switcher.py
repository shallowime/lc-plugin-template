#
# @lc app=leetcode.cn id=319 lang=python3
# @lcpr version=30201
#
# [319] 灯泡开关
#

import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.bulbSwitch(3))
    print(solution.bulbSwitch(0))
    print(solution.bulbSwitch(1))



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


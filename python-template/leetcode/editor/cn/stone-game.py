#
# @lc app=leetcode.cn id=877 lang=python3
# @lcpr version=30201
#
# [877] 石子游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.stoneGame([5,3,4,5]))
    print(solution.stoneGame([3,7,2,3]))



#
# @lcpr case=start
# [5,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,7,2,3]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=1514 lang=python3
# @lcpr version=30201
#
# [1514] 概率最大的路径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.3]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1]]\n[0.5]\n0\n2\n
# @lcpr case=end

#


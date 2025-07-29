#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=30201
#
# [77] 组合
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0 or n <= 0:
            return self.res
        track = []
        self.backtrack(n, k, 1, track)
        return self.res
    
    def backtrack(self, n: int, k: int, start: int, track: List[int]):
        if k == len(track):
            self.res.append(track.copy())
            return
        
        for i in range(start, n + 1):
            track.append(i)
            self.backtrack(n, k, i + 1, track)
            track.pop()
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))



#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#


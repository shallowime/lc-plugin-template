#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30201
#
# [200] 岛屿数量
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res
    
    def dfs(self, grid: List[List[str]], i: int, j: int):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))



#
# @lcpr case=start
# [\n["1","1","1","1","0"],\n["1","1","0","1","0"],\n["1","1","0","0","0"],\n["0","0","0","0","0"]\n]\n
# @lcpr case=end

# @lcpr case=start
# [\n["1","1","0","0","0"],\n["1","1","0","0","0"],\n["0","0","1","0","0"],\n["0","0","0","1","1"]\n]\n
# @lcpr case=end

#


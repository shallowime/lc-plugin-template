#
# @lc app=leetcode.cn id=1254 lang=python3
# @lcpr version=30201
#
# [1254] 统计封闭岛屿的数目
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            self.dfs(grid, i, 0)
            self.dfs(grid, i, n - 1)
        for j in range(n):
            self.dfs(grid, 0, j)
            self.dfs(grid, m - 1, j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid, i, j)
        return res
    
    def dfs(self, grid: List[List[int]], i: int, j: int):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j] == 1:
            return
        grid[i][j] = 1
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))



#
# @lcpr case=start
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1,1,1,1,1],\n[1,0,0,0,0,0,1],\n[1,0,1,1,1,0,1],\n[1,0,1,0,1,0,1],\n[1,0,1,1,1,0,1],\n[1,0,0,0,0,0,1],\n[1,1,1,1,1,1,1]]\n
# @lcpr case=end

#


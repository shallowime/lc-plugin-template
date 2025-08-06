#
# @lc app=leetcode.cn id=1091 lang=python3
# @lcpr version=30201
#
# [1091] 二进制矩阵中的最短路径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from collections import deque

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        
        q = deque([(0, 0)])
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[0][0] = True
        step = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == (m-1, n-1):
                    return step + 1
                
                for dir in dirs:
                    x = cur[0] + dir[0]
                    y = cur[1] + dir[1]
                    if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or grid[x][y] == 1:
                        continue
                    q.append((x, y))
                    visited[x][y] = True
            step += 1
        return -1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPathBinaryMatrix([[0,1],[1,0]]))



#
# @lcpr case=start
# [[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[1,1,0],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0],[1,1,0],[1,1,0]]\n
# @lcpr case=end

#


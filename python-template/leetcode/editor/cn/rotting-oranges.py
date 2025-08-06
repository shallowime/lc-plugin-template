#
# @lc app=leetcode.cn id=994 lang=python3
# @lcpr version=30201
#
# [994] 腐烂的橘子
#

import sys
import os
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                point = q.popleft()
                for dir in dirs:
                    x = point[0] + dir[0]
                    y = point[1] + dir[1]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
            step += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return step - 1 if step else 0

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))



#
# @lcpr case=start
# [[2,1,1],[1,1,0],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,1],[0,1,1],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2]]\n
# @lcpr case=end

#


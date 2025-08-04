#
# @lc app=leetcode.cn id=980 lang=python3
# @lcpr version=30201
#
# [980] 不同路径 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.res = 0                    # 记录所有可行路径的数量
        self.visited = None             # 记录每个格子是否被访问过
        self.visited_count = 0          # 当前已访问的格子数量
        self.total_count = 0            # 需要访问的总格子数量（起点+可访问格子）
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 四个方向：上、下、左、右
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 初始化访问矩阵
        self.visited = [[False] * n for _ in range(m)]

        # 找到起点位置，并计算需要访问的总格子数
        startI, startJ = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # 找到起点
                    startI, startJ = i, j
                if grid[i][j] == 1 or grid[i][j] == 0:  # 统计需要访问的格子
                    self.total_count += 1

        # 从起点开始DFS
        self.dfs(grid, startI, startJ)
        return self.res
    
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        
        # 边界检查：超出网格范围
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        
        # 障碍物检查：遇到障碍物或已访问的格子
        if grid[i][j] == -1 or self.visited[i][j]:
            return
        
        # 到达终点检查
        if grid[i][j] == 2:
            # 只有当访问了所有需要访问的格子时，才是一条有效路径
            if self.visited_count == self.total_count:
                self.res += 1
            return
        
        # 标记当前格子为已访问
        self.visited[i][j] = True
        self.visited_count += 1

        # 尝试四个方向
        for dir in self.dirs:
            self.dfs(grid, i + dir[0], j + dir[1])

        # 回溯：撤销当前选择
        self.visited[i][j] = False
        self.visited_count -= 1
# @lc code=end

def demonstrate_algorithm():
    """
    演示算法工作原理
    以测试用例 [[1,0,0,0],[0,0,0,0],[0,0,2,-1]] 为例
    """
    print("=== Unique Paths III 算法演示 ===")
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print("网格:")
    for row in grid:
        print(f"  {row}")
    print()
    
    print("网格说明:")
    print("  1: 起点")
    print("  0: 可访问的格子")
    print("  2: 终点")
    print("  -1: 障碍物")
    print()
    
    print("算法步骤:")
    print("1. 统计需要访问的格子总数: 起点(1) + 可访问格子(0) = 8个")
    print("2. 从起点(0,0)开始DFS")
    print("3. 每次访问一个格子，标记为已访问")
    print("4. 尝试四个方向：上、下、左、右")
    print("5. 到达终点时，检查是否访问了所有8个格子")
    print("6. 如果是，则找到一条有效路径")
    print("7. 回溯时撤销访问标记")
    print()
    
    print("关键点:")
    print("- visited_count 记录当前路径已访问的格子数")
    print("- total_count 记录需要访问的总格子数")
    print("- 只有 visited_count == total_count 时，到达终点才算有效路径")
    print("- 回溯时一定要撤销访问标记，否则会影响其他路径")

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    result = solution.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    print(f"结果: {result}")
    print()
    demonstrate_algorithm()



#
# @lcpr case=start
# [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0],[0,0,0,0],[0,0,0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[2,0]]\n
# @lcpr case=end

#


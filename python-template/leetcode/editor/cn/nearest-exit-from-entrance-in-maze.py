#
# @lc app=leetcode.cn id=1926 lang=python3
# @lcpr version=30201
#
# [1926] 迷宫中离入口最近的出口
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from collections import deque
# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 四个方向：右、左、下、上

        quene = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        quene.append(entrance)
        visited[entrance[0]][entrance[1]] = True
        step = 0
        
        while quene:
            sz = len(quene)  # 当前层的节点数量
            step += 1        # 进入新的一层，步数+1
            # 注意：step += 1 在 for 循环前，因为：
            # 1. 层序遍历中，每处理完一层，步数就+1
            # 2. 当前层的所有节点都在同一距离（步数）上
            # 3. 处理完当前层后，下一层的节点距离起点都+1步
            
            for _ in range(sz):  # 处理当前层的所有节点
                cur = quene.popleft()
                for dir in dirs:
                    x = cur[0] + dir[0]
                    y = cur[1] + dir[1]
                    # 边界检查或障碍物检查
                    if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or maze[x][y] == '+':
                        continue
                    # 找到出口（边界）
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return step
                    visited[x][y] = True
                    quene.append((x, y))
        return -1
# @lc code=end

def demonstrate_bfs_layers():
    """
    演示BFS层序遍历和step计数的工作原理
    """
    print("=== BFS层序遍历演示 ===")
    print("迷宫:")
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    for row in maze:
        print(f"  {row}")
    print("入口: [1,2]")
    print()
    
    print("BFS层序遍历过程:")
    print("第0层 (step=0): 起点 [1,2]")
    print("第1层 (step=1): [1,1], [1,3], [0,2], [2,2]")
    print("第2层 (step=2): [0,1], [0,3], [2,1], [2,3]")
    print()
    
    print("关键理解:")
    print("1. step += 1 在 for 循环前：")
    print("   - 每进入新的一层，步数就+1")
    print("   - 当前层的所有节点都在同一距离上")
    print("   - 处理完当前层后，下一层节点距离起点都+1步")
    print()
    print("2. 如果 step += 1 在 for 循环后：")
    print("   - 会漏掉第一层的步数")
    print("   - 或者会多计算一层")
    print()
    print("3. 层序遍历的核心：")
    print("   - 同一层的所有节点距离起点相同")
    print("   - 先处理完当前层，再处理下一层")
    print("   - 每层处理完，步数+1")

if __name__ == '__main__':
    solution = Solution()
    result = solution.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2])
    print(f"结果: {result}")
    print()
    demonstrate_bfs_layers()



#
# @lcpr case=start
# [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# [["+","+","+"],[".",".","."],["+","+","+"]]\n[1,0]\n
# @lcpr case=end

# @lcpr case=start
# [[".","+"]]\n[0,0]\n
# @lcpr case=end

#


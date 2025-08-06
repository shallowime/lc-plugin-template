#
# @lc app=leetcode.cn id=365 lang=python3
# @lcpr version=30201
#
# [365] 水壶问题
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from collections import deque
# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        q = deque()
        # 用来记录已经遍历过的状态，把元组转化成数字方便存储哈希集合
        # 转化方式是 (x, y) -> (x * (jug2Capacity + 1) + y)，和二维数组坐标转一维坐标是一样的原理
        # 因为水桶 2 的取值是 [0, jug2Capacity]，所以需要额外加一，请类比二维数组坐标转一维坐标
        # 且考虑到题目输入的数据规模较大，相乘可能导致 int 溢出，所以使用 long 类型
        visited = set()
        # 添加初始状态，两个桶都没有水
        q.append((0, 0))
        visited.add(0 * (y + 1) + 0)

        while q:
            curState = q.popleft()
            if (curState[0] == target or curState[1] == target or curState[0] + curState[1] == target):
                return True
            
            nextStates = []
            # 把 1 桶灌满
            nextStates.append((x, curState[1]))
            # 把 2 桶灌满
            nextStates.append((curState[0], y))
            # 把 1 桶倒空
            nextStates.append((0, curState[1]))
            # 把 2 桶倒空
            nextStates.append((curState[0], 0))
            # 把 1 桶的水灌进 2 桶，直到 1 桶空了或者 2 桶满了
            nextStates.append((curState[0] - min(curState[0], y - curState[1]), curState[1] + min(curState[0], y - curState[1])))
            # 把 2 桶的水灌进 1 桶，直到 2 桶空了或者 1 桶满了
            nextStates.append((curState[0] + min(curState[1], x - curState[0]), curState[1] - min(curState[1], x - curState[0])))

            for nextState in nextStates:
                hashValue = nextState[0] * (y + 1) + nextState[1]
                if hashValue in visited:
                    continue
                q.append(nextState)
                visited.add(hashValue)
        return False

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.canMeasureWater(3, 5, 4))



#
# @lcpr case=start
# 3\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n6\n5\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n3\n
# @lcpr case=end

#


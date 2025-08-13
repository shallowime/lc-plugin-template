#
# @lc app=leetcode.cn id=210 lang=python3
# @lcpr version=30201
#
# [210] 课程表 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.onPath = []
        self.visited = []
        self.hasCycle = False
        self.postOrder = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.buildGraph(numCourses, prerequisites)
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses

        for i in range(numCourses):
            self.traverse(graph, i)

        if self.hasCycle:
            return []
        self.postOrder.reverse()
        return self.postOrder
    
    def traverse(self, graph: List[List[int]], s: int) -> None:
        if self.onPath[s]:
            self.hasCycle = True

        if self.hasCycle or self.visited[s]:
            return
        
        self.onPath[s] = True
        self.visited[s] = True

        for t in graph[s]:
            self.traverse(graph, t)

        self.postOrder.append(s)
        self.onPath[s] = False

    def buildGraph(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            from_node = edge[1]
            to_node = edge[0]
            graph[from_node].append(to_node)
        return graph

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(2, [[1,0]]))
    print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(solution.findOrder(1, []))



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[1,0],[2,0],[3,1],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[]\n
# @lcpr case=end

#


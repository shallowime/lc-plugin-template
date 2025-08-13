#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30201
#
# [207] 课程表
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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)
        self.visited = [False] * numCourses
        self.onPath = [False] * numCourses

        for i in range(numCourses):
            self.traverse(graph, i)
        return not self.hasCycle
    
    def traverse(self, graph: List[List[int]], s: int) -> None:
        if self.onPath[s]:
            self.hasCycle = True
            
        if self.visited[s] or self.hasCycle:
            return
        
        self.visited[s] = True
        self.onPath[s] = True
        for t in graph[s]:
            self.traverse(graph, t)

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
    print(solution.canFinish(2, [[1,0]]))
    print(solution.canFinish(2, [[1,0],[0,1]]))



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#


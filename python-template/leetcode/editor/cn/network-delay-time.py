#
# @lc app=leetcode.cn id=743 lang=python3
# @lcpr version=30201
#
# [743] 网络延迟时间
#

import sys
import os
import heapq
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            graph[i] = []
        for edge in times:
            from_node = edge[0]
            to_node = edge[1]
            weight = edge[2]
            graph[from_node].append((to_node, weight))

        distTo = self.dijkstra(graph, k)

        res = 0
        for i in range(1, len(distTo)):
            if distTo[i] == float('inf'):
                return -1
            res = max(res, distTo[i])
        return res
    
    class State:
        def __init__(self, id, distFromStart):
            self.id = id
            self.distFromStart = distFromStart

    def dijkstra(self, graph, start):
        distTo = [float('inf')] * len(graph)
        distTo[start] = 0

        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            curDistFromStart, curNodeId = heapq.heappop(pq)

            if curDistFromStart > distTo[curNodeId]:
                continue

            for nextNodeID, weight in graph[curNodeId]:
                distToNextNode = distTo[curNodeId] + weight
                if distToNextNode < distTo[nextNodeID]:
                    distTo[nextNodeID] = distToNextNode
                    heapq.heappush(pq, (distToNextNode, nextNodeID))
        return distTo
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))



#
# @lcpr case=start
# [[2,1,1],[2,3,1],[3,4,1]]\n4\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1]]\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1]]\n2\n2\n
# @lcpr case=end

#


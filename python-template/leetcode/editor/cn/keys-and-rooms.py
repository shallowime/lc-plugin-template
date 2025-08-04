#
# @lc app=leetcode.cn id=841 lang=python3
# @lcpr version=30201
#
# [841] 钥匙和房间
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from collections import deque
from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        queue = deque([0])
        visited[0] = True

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        return all(visited)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.canVisitAllRooms([[1],[2],[3],[]]))



#
# @lcpr case=start
# [[1],[2],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[3,0,1],[2],[0]]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=773 lang=python3
# @lcpr version=30201
#
# [773] 滑动谜题
#

import sys
import os
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        start = ''.join(str(num) for row in board for num in row)

        neighbor = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]

        q = deque([start])
        visited = set([start])

        step = 0

        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == target:
                    return step
                
                idx = cur.index('0')

                for adj in neighbor[idx]:
                    new_board = self.swap(list(cur), idx, adj)
                    if new_board not in visited:
                        q.append(new_board)
                        visited.add(new_board)
            step += 1
        return -1

    def swap(self, board, i, j):
        board[i], board[j] = board[j], board[i]
        return ''.join(board)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.slidingPuzzle([[4,1,2],[5,0,3]]))


#
# @lcpr case=start
# [[1,2,3],[4,0,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,4,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,1,2],[5,0,3]]\n
# @lcpr case=end

#


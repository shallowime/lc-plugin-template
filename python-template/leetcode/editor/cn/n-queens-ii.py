#
# @lc app=leetcode.cn id=52 lang=python3
# @lcpr version=30201
#
# [52] N 皇后 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        board = ["." * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.res
    
    def backtrack(self, board: List[str], row: int):
        if row == len(board):
            self.res += 1
            return
        
        n = len(board)
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
            
            board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
            self.backtrack(board, row + 1)
            board[row] = board[row][:col] + '.' + board[row][col + 1:]

    def isValid(self, board: List[str], row: int, col: int) -> bool:
        n = len(board)
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        return True

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(4))



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


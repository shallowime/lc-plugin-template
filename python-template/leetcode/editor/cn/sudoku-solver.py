#
# @lc app=leetcode.cn id=37 lang=python3
# @lcpr version=30201
#
# [37] 解数独
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 标记是否已经找到可行解
        self.found = False
        self.backtrack(board, 0)

    def backtrack(self, board: List[List[str]], index: int):
        # 如果已经找到可行解，则直接返回
        if self.found:
            return
        
        m, n = 9, 9
        i, j = index // n, index % n
        if index == m * n:
            # 找到可行解
            self.found = True
            return
        
        # 如果当前位置已经有数字，则直接跳过
        if board[i][j] != '.':
            self.backtrack(board, index + 1)
            return  # 添加这个 return 语句！
        
        for ch in '123456789':
            if not self.isValid(board, i, j, ch):
                continue

            board[i][j] = ch
            
            self.backtrack(board, index + 1)
            if self.found:
                # 如果已经找到可行解，则直接返回
                # 不要撤销选择，不然board[i][j]会变成'.'
                return
            
            # 撤销选择
            board[i][j] = '.'

    def isValid(self, board: List[List[str]], r: int, c: int, num: str) -> bool:
        for k in range(9):
            if board[r][k] == num:
                return False
            if board[k][c] == num:
                return False
            if board[(r // 3) * 3 + k // 3][(c // 3) * 3 + k % 3] == num:
                return False
        return True
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    solution.solveSudoku(board)
    print(board)



#
# @lcpr case=start
# \n[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#


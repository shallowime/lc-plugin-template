#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30201
#
# [79] 单词搜索
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.found = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, word, 0)
                if self.found:
                    return True
        return False
    
    def dfs(self, board, i, j, word, p):
        if p == len(word):
            self.found = True
            return 
        
        if self.found:
            return
        
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] != word[p]:
            return
        
        temp = board[i][j]
        board[i][j] = '#'
        self.dfs(board, i + 1, j, word, p + 1)
        self.dfs(board, i - 1, j, word, p + 1)
        self.dfs(board, i, j + 1, word, p + 1)
        self.dfs(board, i, j - 1, word, p + 1)
        board[i][j] = temp
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))



#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

#


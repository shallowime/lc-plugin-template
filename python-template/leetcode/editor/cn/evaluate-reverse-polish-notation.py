#
# @lc app=leetcode.cn id=150 lang=python3
# @lcpr version=30201
#
# [150] 逆波兰表达式求值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                right = stk.pop()
                left = stk.pop()
                stk.append(self.calc(left, right, token))
            else:
                stk.append(int(token))
        return stk[0]

    def calc(self, left: int, right: int, token: str) -> int:
        if token == '+':
            return left + right
        if token == '-':
            return left - right
        if token == '*':
            return left * right
        return int(left / right)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.evalRPN(["2","1","+","3","*"]))
    print(solution.evalRPN(["4","13","5","/","+"]))
    print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#


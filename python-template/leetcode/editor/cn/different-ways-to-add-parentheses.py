#
# @lc app=leetcode.cn id=241 lang=python3
# @lcpr version=30201
#
# [241] 为运算表达式设计优先级
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]
        
        res = []
        for i in range(len(expression)):
            c = expression[i]
            if c == '-' or c == '+' or c == '*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                for a in left:
                    for b in right:
                        if c == "+":
                            res.append(a + b)
                        elif c == "-":
                            res.append(a - b)
                        elif c == "*":
                            res.append(a * b)
        
        if not res:
            res.append(int(expression))

        self.memo[expression] = res
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.diffWaysToCompute("2-1-1"))
    print(solution.diffWaysToCompute("2*3-4*5"))



#
# @lcpr case=start
# "2-1-1"\n
# @lcpr case=end

# @lcpr case=start
# "2*3-4*5"\n
# @lcpr case=end

#


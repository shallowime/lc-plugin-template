#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30201
#
# [20] 有效的括号
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        for c in s:
            if c in ['(', '{', '[']:
                left.append(c)
            else:
                if left and self.leftOf(c) == left[-1]:
                    left.pop()
                else:
                    return False
        return len(left) == 0

    def leftOf(self, c: str) -> str:
        if c == ')':
            return '('
        if c == '}':
            return '{'
        return '['
# @lc code=end

if __name__ == '__main__':
    solution = Solution()   
    # your test code here
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([)]"))
    print(solution.isValid("{[]}"))


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#


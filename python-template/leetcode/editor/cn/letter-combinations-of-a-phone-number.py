#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30201
#
# [17] 电话号码的字母组合
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.phoneMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return self.res
        
        self.backtrack(digits, 0)
        return self.res
    
    def backtrack(self, digits, start):
        if len(self.track) == len(digits):
            self.res.append("".join(self.track))
            return
        
        digit = digits[start]
        for c in self.phoneMap[digit]:
            self.track.append(c)
            self.backtrack(digits, start + 1)
            self.track.pop()
        
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.letterCombinations("23"))


#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#


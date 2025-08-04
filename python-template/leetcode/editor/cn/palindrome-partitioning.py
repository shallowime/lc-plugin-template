#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30201
#
# [131] 分割回文串
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

    def partition(self, s: str) -> List[List[str]]:
        self.backtrack(s, 0)
        return self.res
    
    def backtrack(self, s, start):
        if start == len(s):
            self.res.append(self.track.copy())
            return
        
        for i in range(start, len(s)):
            if not self.isPalindrome(s, start, i):
                continue

            self.track.append(s[start:i+1])
            self.backtrack(s, i+1)
            self.track.pop()

    def isPalindrome(self, s, left, right):
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.partition("aab"))


#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#


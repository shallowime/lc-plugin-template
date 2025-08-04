#
# @lc app=leetcode.cn id=93 lang=python3
# @lcpr version=30201
#
# [93] 复原 IP 地址
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

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtrack(s, 0)
        return self.res
    
    def backtrack(self, s, start):
        if len(self.track) == 4 and start == len(s):
            self.res.append(".".join(self.track))

        for i in range(start, len(s)):
            if not self.isValid(s, start, i):
                continue

            if len(self.track) >= 4:
                break

            self.track.append(s[start:i+1])
            self.backtrack(s, i+1)
            self.track.pop()

    def isValid(self, s, left, right):
        length = right - left + 1
        if length == 0 or length > 3:
            return False
        
        if length == 1:
            return True
        
        if s[left] == '0':
            return False
        
        if length <= 2:
            return True
        
        if int(s[left:right+1]) > 255:
            return False
        
        return True

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.restoreIpAddresses("25525511135"))


#
# @lcpr case=start
# "25525511135"\n
# @lcpr case=end

# @lcpr case=start
# "0000"\n
# @lcpr case=end

# @lcpr case=start
# "101023"\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30201
#
# [151] 反转字符串中的单词
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        res = ''
        for i in range(len(s)):
            s_ = s.pop()
            res += s_
            res += ' '
        return res[:-1]
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.reverseWords("the sky is blue")) 


#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#


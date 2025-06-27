#
# @lc app=leetcode.cn id=71 lang=python3
# @lcpr version=30201
#
# [71] 简化路径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stk = []
        for part in parts:
            if part == '..':
                if stk:
                    stk.pop()
            elif part == '.' or part == '':
                continue
            else:
                stk.append(part)

        return '/' + '/'.join(stk)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.simplifyPath("/home/"))
    print(solution.simplifyPath("/home//foo/"))
    print(solution.simplifyPath("/home/user/Documents/../Pictures"))
    print(solution.simplifyPath("/../"))
    print(solution.simplifyPath("/.../a/../b/c/../d/./"))


#
# @lcpr case=start
# "/home/"\n
# @lcpr case=end

# @lcpr case=start
# "/home//foo/"\n
# @lcpr case=end

# @lcpr case=start
# "/home/user/Documents/../Pictures"\n
# @lcpr case=end

# @lcpr case=start
# "/../"\n
# @lcpr case=end

# @lcpr case=start
# "/.../a/../b/c/../d/./"\n
# @lcpr case=end

#


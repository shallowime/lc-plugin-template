#
# @lc app=leetcode.cn id=402 lang=python3
# @lcpr version=30201
#
# [402] 移掉 K 位数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for c in num:
            while stk and stk[-1] > c and k > 0:
                stk.pop()
                k -= 1
            if not stk and c == '0':
                continue
            stk.append(c)

        final_stk = stk[:-k] if k > 0 else stk
        result = ''.join(final_stk).lstrip('0')
        return result if result else '0'
    

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeKdigits("1432219", 3))
    print(solution.removeKdigits("10200", 1))
    print(solution.removeKdigits("10", 2))



#
# @lcpr case=start
# "1432219"\n3\n
# @lcpr case=end

# @lcpr case=start
# "10200"\n1\n
# @lcpr case=end

# @lcpr case=start
# "10"\n2\n
# @lcpr case=end

#


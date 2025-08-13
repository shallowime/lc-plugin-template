#
# @lc app=leetcode.cn id=372 lang=python3
# @lcpr version=30201
#
# [372] 超级次方
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.base = 1337

    def superPow(self, a: int, b: List[int]) -> int:
        if len(b) == 0:
            return 1
        last = b[-1]
        newB = b[:-1]
        part1 = self.mypow(a, last)
        part2 = self.mypow(self.superPow(a, newB), 10)
        return (part1 * part2) % self.base
    
    def mypow(self, a: int, k: int) -> int:
        a %= self.base
        res = 1
        for i in range(k):
            res *= a
            res %= self.base
        return res
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.superPow(2, [3]))
    print(solution.superPow(2, [1,0]))
    print(solution.superPow(1, [4,3,3,8,5,2]))
    print(solution.superPow(2147483647, [2,0,0]))



#
# @lcpr case=start
# 2\n[3]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,0]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[4,3,3,8,5,2]\n
# @lcpr case=end

# @lcpr case=start
# 2147483647\n[2,0,0]\n
# @lcpr case=end

#


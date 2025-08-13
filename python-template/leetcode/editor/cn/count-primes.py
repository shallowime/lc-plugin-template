#
# @lc app=leetcode.cn id=204 lang=python3
# @lcpr version=30201
#
# [204] 计数质数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10))
    print(solution.countPrimes(0))
    print(solution.countPrimes(1))



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


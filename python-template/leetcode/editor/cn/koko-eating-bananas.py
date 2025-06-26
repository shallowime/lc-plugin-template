#
# @lc app=leetcode.cn id=875 lang=python3
# @lcpr version=30201
#
# [875] 爱吃香蕉的珂珂
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if self.f(piles, mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def f(self, piles: List[int], speed: int) -> int:
        hours = 0
        for pile in piles:
            hours += pile // speed
            if pile % speed != 0:
                hours += 1
        return hours
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.minEatingSpeed([3, 6, 7, 11], 8))
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))


#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#


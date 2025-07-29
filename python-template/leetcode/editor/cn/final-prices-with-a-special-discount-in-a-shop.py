#
# @lc app=leetcode.cn id=1475 lang=python3
# @lcpr version=30201
#
# [1475] 商品折扣后的最终价格
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = [0] * n
        next_element = self.nextLessOrEqualElement(prices)
        for i in range(n):
            if next_element[i] != -1:
                res[i] = prices[i] - next_element[i]
            else:
                res[i] = prices[i]
        return res

    def nextLessOrEqualElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and stk[-1] > nums[i]:
                stk.pop()
            res[i] = stk[-1] if stk else -1
            stk.append(nums[i])
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.finalPrices([8,4,6,2,3]))



#
# @lcpr case=start
# [8,4,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [10,1,1,6]\n
# @lcpr case=end

#


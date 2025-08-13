#
# @lc app=leetcode.cn id=528 lang=python3
# @lcpr version=30201
#
# [528] 按权重随机选择
#

import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            self.preSum[i] = self.preSum[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        n = len(self.preSum)
        target = random.randint(1, self.preSum[n - 1])
        return self.left_bound(self.preSum, target) - 1
    
    def left_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

if __name__ == '__main__':
    solution = Solution([1,3])
    print(solution.pickIndex())
    print(solution.pickIndex())



#
# @lcpr case=start
# ["Solution","pickIndex"]\n[[[1]],[]]\n
# @lcpr case=end

# @lcpr case=start
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]\n[[[1,3]],[],[],[],[],[]]\n
# @lcpr case=end

#


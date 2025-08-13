#
# @lc app=leetcode.cn id=384 lang=python3
# @lcpr version=30201
#
# [384] 打乱数组
#

import sys
import os
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

if __name__ == '__main__':
    solution = Solution([1, 2, 3])
    # your test code nums = [1, 2, 3]
    print(solution.reset())
    print(solution.shuffle())
    print(solution.reset())




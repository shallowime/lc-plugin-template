#
# @lc app=leetcode.cn id=398 lang=python3
# @lcpr version=30201
#
# [398] 随机数索引
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
        self.indices = {}
        for index, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(index)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

if __name__ == '__main__':
    solution = Solution([1, 2, 3, 3, 3])
    # your test code here
    print(solution.pick(3))
    print(solution.pick(1))
    print(solution.pick(3))




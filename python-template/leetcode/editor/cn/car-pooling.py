#
# @lc app=leetcode.cn id=1094 lang=python3
# @lcpr version=30201
#
# [1094] 拼车
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0] * 1001
        df = Difference(nums)
        for trip in trips:
            # 第 trip[1] 站乘客上车
            i = trip[1]
            # 第 trip[2] 站乘客已经下车，
            # 即乘客在车上的区间是 [trip[1], trip[2] - 1]
            j = trip[2] - 1
            # 乘客数量
            val = trip[0]
            # 对区间 [i, j] 上车的乘客数量进行增量
            df.increment(i, j, val)
        res = df.result()

        for i in range(len(res)):
            if res[i] > capacity:
                return False
        return True

class Difference:
    def __init__(self, nums: List[int]):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]
            
    def increment(self, i: int, j: int, val: int):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.carPooling([[2, 1, 5], [3, 3, 7]], 4))
    print(solution.carPooling([[2, 1, 5], [3, 3, 7]], 5))



#
# @lcpr case=start
# [[2,1,5],[3,3,7]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,5],[3,3,7]]\n5\n
# @lcpr case=end

#


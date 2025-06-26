#
# @lc app=leetcode.cn id=1011 lang=python3
# @lcpr version=30201
#
# [1011] 在 D 天内送达包裹的能力
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if self.f(weights, mid) <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left

    # 定义：当运载能力为 x 时，需要 f(x) 天运完所有货物
    # f(x) 随着 x 的增加单调递减
    def f(self, weights: List[int], x: int) -> int:
        days = 0
        # 初始化货物索引
        i = 0
        # 外循环：每次代表一天的运输
        while i < len(weights):
            # 每天开始时，船的容量重置为x
            cap = x
            # 内循环：尝试在当天装载尽可能多的货物
            while i < len(weights):
                if weights[i] > cap: # 当前货物装不下了
                    break # 结束今天的装载
                else:
                    cap -= weights[i] # 减少剩余容量
                    i += 1 # 移到下一个货物
            days += 1 # 当天装载结束，天数+1
        return days # 返回总共需要的天数
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(solution.shipWithinDays([3, 2, 2, 4, 1, 4], 3))
    print(solution.shipWithinDays([1, 2, 3, 1, 1], 4))


#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#


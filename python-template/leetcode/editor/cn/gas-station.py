#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30201
#
# [134] 加油站
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0
        current_tank = 0
        start_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                start_station = i + 1
                current_tank = 0
        return -1 if total_tank < 0 else start_station

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(solution.canCompleteCircuit([2,3,4], [3,4,3]))



#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=2073 lang=python3
# @lcpr version=30201
#
# [2073] 买票需要的时间
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.timeRequiredToBuy([2,3,2], 2))
    print(solution.timeRequiredToBuy([5,1,1,1], 0))



#
# @lcpr case=start
# [2,3,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,1]\n0\n
# @lcpr case=end

#


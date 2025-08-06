#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30201
#
# [55] 跳跃游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if farthest <= i:
                return False
        return True

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.canJump([2,3,1,1,4]))
    print(solution.canJump([3,2,1,0,4]))


#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#


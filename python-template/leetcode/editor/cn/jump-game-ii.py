#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30201
#
# [45] 跳跃游戏 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        farthest = 0
        jumps = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if end == i:
                jumps += 1
                end = farthest
        return jumps

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#


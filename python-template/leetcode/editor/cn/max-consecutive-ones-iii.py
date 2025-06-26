#
# @lc app=leetcode.cn id=1004 lang=python3
# @lcpr version=30201
#
# [1004] 最大连续1的个数 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        windowOneCount = 0
        res = 0
        while right < len(nums):
            if nums[right] == 1:
                windowOneCount += 1
            right += 1
            while right - left - windowOneCount > k:
                if nums[left] == 1:
                    windowOneCount -= 1
                left += 1
            res = max(res, right - left)
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))



#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#


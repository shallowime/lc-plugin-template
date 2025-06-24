#
# @lc app=leetcode.cn id=1658 lang=python3
# @lcpr version=30201
#
# [1658] 将 x 减到 0 的最小操作数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sum_ = sum(nums)
        target = sum_ - x

        left, right = 0, 0
        window = 0
        max_length = float('-inf')
        while right < n:
            window += nums[right]
            right += 1
            while window > target and left < right:
                window -= nums[left]
                left += 1
            if window == target:
                max_length = max(max_length, right - left)
        return -1 if max_length == float('-inf') else n - max_length
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=27 lang=python3
# @lcpr version=30201
#
# [27] 移除元素
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [3, 2, 2, 3]
    val = 3
    print(solution.removeElement(nums, val))


#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#


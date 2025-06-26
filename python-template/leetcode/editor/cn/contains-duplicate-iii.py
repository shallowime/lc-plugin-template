#
# @lc app=leetcode.cn id=220 lang=python3
# @lcpr version=30201
#
# [220] 存在重复元素 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedList
        window = SortedList()
        
        for i in range(len(nums)):

            pos = window.bisect_left(nums[i])
            if pos < len(window) and window[pos] - nums[i] <= valueDiff:
                return True
            if pos > 0 and nums[i] - window[pos - 1] <= valueDiff:
                return True
            window.add(nums[i])
            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])
        return False
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))


#
# @lcpr case=start
# [1,2,3,1]\n3\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,5,9,1,5,9]\n2\n3\n
# @lcpr case=end

#


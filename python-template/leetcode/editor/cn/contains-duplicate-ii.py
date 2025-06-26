#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30201
#
# [219] 存在重复元素 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0
        window = set()
        while right < len(nums):

            if nums[right] in window:
                return True
            window.add(nums[right])
            right += 1
            while right - left > k:
                window.remove(nums[left])
                left += 1
        return False
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))


#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#


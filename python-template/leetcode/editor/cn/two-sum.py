#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30201
#
# [1] 两数之和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in val_index:
                return [val_index[need], i]
            val_index[nums[i]] = i
        return []
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
    print(solution.twoSum([3,2,4], 6))
    print(solution.twoSum([3,3], 6))



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#


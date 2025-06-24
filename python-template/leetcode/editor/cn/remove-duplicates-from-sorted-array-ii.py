#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30201
#
# [80] 删除有序数组中的重复项 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        # 快慢指针 维护[0,slow]为结果
        slow, fast = 0, 0
        # 记录当前数字的重复次数
        count = 0

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                # 此时，对于nums[0..slow]来说，nums[fast]是一个新的元素，加进来
                slow += 1
                nums[slow] = nums[fast]
            elif slow < fast and count < 2:
                # 此时，对于nums[0..slow]来说，nums[fast]重复次数小于2，也加进来
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
            count += 1
            if fast < len(nums) and nums[fast] != nums[fast - 1]:
                # fast遇到新的不同的元素时，重置count
                count = 0
        # 数组长度为索引+1
        return slow + 1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums = [1, 1, 1, 2, 2, 3]
    print(solution.removeDuplicates(nums))
    print(nums)


#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#


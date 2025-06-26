#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30201
#
# [713] 乘积小于 K 的子数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        product = 1
        res = 0

        while right < len(nums):
            product *= nums[right]
            right += 1
            while product >= k and left < right:
                product //= nums[left]
                left += 1
            # 现在必然是一个合法的窗口，但注意思考这个窗口中的子数组个数怎么计算：
            # 比方说 left = 1, right = 4 划定了 [1, 2, 3] 这个窗口（right 是开区间）
            # 但不止 [left..right] 是合法的子数组，[left+1..right], [left+2..right] 等都是合法子数组
            # 所以我们需要把 [3], [2,3], [1,2,3] 这 right - left 个子数组都加上
            res += right - left
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(solution.numSubarrayProductLessThanK([1, 2, 3], 0))


#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#


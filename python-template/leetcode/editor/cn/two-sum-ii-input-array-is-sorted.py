#
# @lc app=leetcode.cn id=167 lang=python3
# @lcpr version=30201
#
# [167] 两数之和 II - 输入有序数组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    numbers = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(numbers, target))


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#


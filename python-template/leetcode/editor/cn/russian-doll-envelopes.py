#
# @lc app=leetcode.cn id=354 lang=python3
# @lcpr version=30201
#
# [354] 俄罗斯套娃信封问题
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        height = [envelopes[i][1] for i in range(n)]

        return self.lengthOfLIS(height)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = 0
        n = len(nums)
        top = [0] * n
        for i in range(n):
            poker = nums[i]
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] >= poker:
                    right = mid
                else:
                    left = mid + 1

            if left == piles:
                piles += 1

            top[left] = poker
        return piles
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))



#
# @lcpr case=start
# [[5,4],[6,4],[6,7],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1],[1,1]]\n
# @lcpr case=end

#


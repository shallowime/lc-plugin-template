#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30201
#
# [59] 螺旋矩阵 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        upper_bound, lower_bound = 0, n - 1
        left_bound, right_bound = 0, n - 1
        num = 1
        while num <= n * n:
            if upper_bound <= lower_bound:
                for i in range(left_bound, right_bound + 1):
                    res[upper_bound][i] = num
                    num += 1
                upper_bound += 1
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound + 1):
                    res[i][right_bound] = num
                    num += 1
                right_bound -= 1
            if upper_bound <= lower_bound:
                for i in range(right_bound, left_bound - 1, -1):
                    res[lower_bound][i] = num
                    num += 1
                lower_bound -= 1
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound - 1, -1):
                    res[i][left_bound] = num
                    num += 1
                left_bound += 1
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.generateMatrix(3))


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


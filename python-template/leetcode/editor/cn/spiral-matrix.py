#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30201
#
# [54] 螺旋矩阵
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        upper_bound, lower_bound = 0, m - 1
        left_bound, right_bound = 0, n - 1
        while len(res) < m * n:
            if upper_bound <= lower_bound:
                for i in range(left_bound, right_bound + 1):
                    res.append(matrix[upper_bound][i])
                upper_bound += 1
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound + 1):
                    res.append(matrix[i][right_bound])
                right_bound -= 1
            if upper_bound <= lower_bound:
                for i in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[lower_bound][i])
                lower_bound -= 1
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound - 1, -1):
                    res.append(matrix[i][left_bound])
                left_bound += 1
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#


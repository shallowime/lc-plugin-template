#
# @lc app=leetcode.cn id=1944 lang=python3
# @lcpr version=30201
#
# [1944] 队列中可以看到的人数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n

        # int[] 记录 {身高，小于等于该身高的人数} 二元组
        stk = []
        for i in range(n - 1, -1, -1):
            # 记录右侧比自己矮的人
            count = 0
            # 单调栈模板，计算下一个更大或相等元素（身高）
            while stk and stk[-1] < heights[i]:
                stk.pop()
                count += 1
            # 不仅可以看到比自己矮的人，如果后面存在更高的的人，也可以看到这个高人
            res[i] = count if not stk else count + 1
            stk.append(heights[i])
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.canSeePersonsCount([10,6,8,5,11,9]))



#
# @lcpr case=start
# [10,6,8,5,11,9]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,3,10]\n
# @lcpr case=end

#


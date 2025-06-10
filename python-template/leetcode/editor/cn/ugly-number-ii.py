#
# @lc app=leetcode.cn id=264 lang=python3
# @lcpr version=30201
#
# [264] 丑数 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 可以理解为三个指向有序链表头结点的指针
        p2, p3, p5 = 1, 1, 1
        # 可以理解为三个有序链表的头节点的值
        product2, product3, product5 = 1, 1, 1
         # 可以理解为最终合并的有序链表（结果链表）
        ugly = [0] * (n + 1)
        # 可以理解为结果链表上的指针
        p = 1

        # 开始合并三个有序链表
        while p <= n:
            # 取三个链表的最小结点
            min_val = min(product2, product3, product5)
            # 接到结果链表上
            ugly[p] = min_val
            p += 1
            # 前进对应有序链表上的指针
            if min_val == product2:
                product2 = ugly[p2] * 2
                p2 += 1
            if min_val == product3:
                product3 = ugly[p3] * 3
                p3 += 1
            if min_val == product5:
                product5 = ugly[p5] * 5
                p5 += 1
        # 返回第 n 个丑数
        return ugly[n]

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    res = solution.nthUglyNumber(10)
    print(res)


#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=1201 lang=python3
# @lcpr version=30201
#
# [1201] 丑数 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # 题目说本题结果在 [1, 2 * 10^9] 范围内，
        # 所以就按照这个范围初始化两端都闭的搜索区间
        left, right = 1, int(2e9)
        # 搜索左侧边界的二分搜索
        while left <= right:
            mid = left + (right - left) // 2
            if self.f(mid, a, b, c) < n:
                # [1..mid] 中的元素个数不足 n，所以目标在右侧
                left = mid + 1
            else:
                # [1..mid] 中的元素个数大于 n，所以目标在左侧
                right = mid - 1
        return left
    
    # 计算 [1..num] 之间有多少个能够被 a 或 b 或 c 整除的数字
    def f(self, num: int, a: int, b: int, c: int) -> int:
        setA = num // a
        setB = num // b
        setC = num // c
        setAB = num // self.lcm(a, b)
        setAC = num // self.lcm(a, c)
        setBC = num // self.lcm(b, c)
        setABC = num // self.lcm(self.lcm(a, b), c)
        # 集合论定理：A + B + C - A ∩ B - A ∩ C - B ∩ C + A ∩ B ∩ C
        return setA + setB + setC - setAB - setAC - setBC + setABC
    
    # 计算最大公因数（辗转相除/欧几里得算法）
    def gcd(self, a: int, b: int) -> int:
        if a < b:
            # 保证 a > b
            return self.gcd(b, a)
        if b == 0:
            return a
        return self.gcd(b, a % b)

    # 最小公倍数
    def lcm(self, a: int, b: int) -> int:
        # 最小公倍数就是乘积除以最大公因数
        return a * b // self.gcd(a, b)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.nthUglyNumber(3, 2, 3, 5))
    print(solution.nthUglyNumber(4, 2, 3, 4))
    print(solution.nthUglyNumber(5, 2, 11, 13))



#
# @lcpr case=start
# 3\n2\n3\n5\n
# @lcpr case=end

# @lcpr case=start
# 4\n2\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# 5\n2\n11\n13\n
# @lcpr case=end

#


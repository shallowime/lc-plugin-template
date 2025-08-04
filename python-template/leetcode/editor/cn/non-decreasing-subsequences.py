#
# @lc app=leetcode.cn id=491 lang=python3
# @lcpr version=30201
#
# [491] 非递减子序列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        注意：不能通过排序来避免重复元素，因为：
        1. 题目要求保持原数组的相对顺序
        2. 排序会改变元素的相对位置，产生错误的子序列
        3. 当前使用used集合在每一层避免重复是正确的方法
        """
        if len(nums) == 0:
            return self.res
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums: List[int], start: int) -> None:
        # 当路径长度>=2时，记录结果
        if len(self.track) >= 2:
            self.res.append(self.track[:])

        # 使用集合避免在同一层选择相同元素
        # 注意：used集合的作用域是当前递归层，每次进入新的递归层都会重新创建
        used = set()
        for i in range(start, len(nums)):
            # 跳过已经使用过的元素（同层去重）
            if nums[i] in used:
                continue
            # 跳过不满足非递减条件的元素
            if len(self.track) > 0 and nums[i] < self.track[-1]:
                continue
            
            # 选择当前元素
            self.track.append(nums[i])
            used.add(nums[i])
            self.backtrack(nums, i + 1)
            # 撤销选择 - 注意：不需要从used中移除，因为used是当前层的局部变量
            self.track.pop()
            
        # 当这个函数结束时，used集合会被销毁，下一层递归会创建新的used集合
# @lc code=end

def demonstrate_used_scope():
    """
    演示used集合的作用域示例
    以数组 [4,6,7,7] 为例
    """
    print("=== used集合作用域演示 ===")
    print("数组: [4,6,7,7]")
    print()
    
    print("递归层1 (start=0):")
    print("  used = set()  # 新的空集合")
    print("  i=0: nums[0]=4, used={}, 选择4")
    print("    used.add(4) -> used={4}")
    print("    递归到下一层...")
    print()
    
    print("递归层2 (start=1):")
    print("  used = set()  # 新的空集合（不是上一层的{4}）")
    print("  i=1: nums[1]=6, used={}, 选择6")
    print("    used.add(6) -> used={6}")
    print("    i=2: nums[2]=7, used={6}, 选择7")
    print("      used.add(7) -> used={6,7}")
    print("      i=3: nums[3]=7, used={6,7}, 跳过（重复）")
    print()
    
    print("关键点：")
    print("1. 每层递归都有独立的used集合")
    print("2. 撤销选择时不需要从used中移除，因为used是局部变量")
    print("3. 函数结束时used自动销毁")

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.findSubsequences([4,6,7,7]))
    print(solution.findSubsequences([4,4,3,2,1]))
    print()
    demonstrate_used_scope()


#
# @lcpr case=start
# [4,6,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,3,2,1]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=95 lang=python3
# @lcpr version=30201
#
# [95] 不同的二叉搜索树 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.build(1, n)

    def build(self, lo:int, hi:int) -> List[Optional[TreeNode]]:
        res = []
        if lo > hi:
            res.append(None)
            return res
        for i in range(lo, hi + 1):
            left = self.build(lo, i - 1)
            right = self.build(i + 1, hi)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateTrees(3))



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


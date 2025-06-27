#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30201
#
# [230] 二叉搜索树中第 K 小的元素
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
    def __init__(self):
        self.res = 0
        self.count = 0
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.res

    def traverse(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return
        self.traverse(root.left, k)
        self.count += 1
        if self.count == k:
            self.res = root.val
            return
        self.traverse(root.right, k)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.kthSmallest(TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1))



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#


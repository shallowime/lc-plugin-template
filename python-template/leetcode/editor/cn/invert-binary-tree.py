#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30201
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.traverse(root.left)
        self.traverse(root.right)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))))


#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


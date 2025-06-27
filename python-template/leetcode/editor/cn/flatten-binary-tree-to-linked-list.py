#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30201
#
# [114] 二叉树展开为链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        left = root.left
        right = root.right
        self.flatten(left)
        self.flatten(right)
        root.left = None
        root.right = left
        while root.right is not None:
            root = root.right
        root.right = right
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.flatten(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))))


#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=106 lang=python3
# @lcpr version=30201
#
# [106] 从中序与后序遍历序列构造二叉树
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
        self.val_to_index = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.val_to_index[inorder[i]] = i
        return self.build(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

    def build(self, inorder: List[int], postorder: List[int], in_start: int, in_end: int, post_start: int, post_end: int) -> Optional[TreeNode]:
        if in_start > in_end:
            return None
        
        root_val = postorder[post_end]
        index = self.val_to_index[root_val]
        left_size = index - in_start

        root = TreeNode(root_val)
        root.left = self.build(inorder, postorder, in_start, index - 1, post_start, post_start + left_size - 1)
        root.right = self.build(inorder, postorder, index + 1, in_end, post_start + left_size, post_end - 1)
        return root

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.buildTree([9,3,15,20,7], [9,15,7,20,3]))


#
# @lcpr case=start
# [9,3,15,20,7]\n[9,15,7,20,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#


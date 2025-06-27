#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30201
#
# [105] 从前序与中序遍历序列构造二叉树
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

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.val_to_index[inorder[i]] = i
        return self.build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def build(self, preorder: List[int], inorder: List[int], pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None
        
        root_val = preorder[pre_start]
        index = self.val_to_index[root_val]
        left_size = index - in_start

        root = TreeNode(root_val)
        root.left = self.build(preorder, inorder, pre_start + 1, pre_start + left_size, in_start, index - 1)
        root.right = self.build(preorder, inorder, pre_start + left_size + 1, pre_end, index + 1, in_end)
        return root

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.buildTree([3,9,20,15,7], [9,3,15,20,7]))


#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#


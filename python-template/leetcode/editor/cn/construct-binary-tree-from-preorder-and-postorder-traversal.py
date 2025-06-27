#
# @lc app=leetcode.cn id=889 lang=python3
# @lcpr version=30201
#
# [889] 根据前序和后序遍历构造二叉树
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

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(postorder)):
            self.val_to_index[postorder[i]] = i
        return self.build(preorder, postorder, 0, len(preorder) - 1, 0, len(postorder) - 1)

    def build(self, preorder: List[int], postorder: List[int], pre_start: int, pre_end: int, post_start: int, post_end: int) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])
        
        root_val = preorder[pre_start]
        leftRootVal = preorder[pre_start + 1]
        index = self.val_to_index[leftRootVal]
        leftSize = index - post_start + 1
        root = TreeNode(root_val)
        root.left = self.build(preorder, postorder, pre_start + 1, pre_start + leftSize, post_start, index)
        root.right = self.build(preorder, postorder, pre_start + leftSize + 1, pre_end, index + 1, post_end - 1)
        return root

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1]\n
# @lcpr case=end

#


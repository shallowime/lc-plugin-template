#
# @lc app=leetcode.cn id=700 lang=python3
# @lcpr version=30201
#
# [700] 二叉搜索树中的搜索
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 2))



#
# @lcpr case=start
# [4,2,7,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,7,1,3]\n5\n
# @lcpr case=end

#


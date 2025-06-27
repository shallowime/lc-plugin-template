#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30201
#
# [98] 验证二叉搜索树
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, None, None)

    def isValid(self, root: Optional[TreeNode], min: Optional[int], max: Optional[int]) -> bool:
        if root is None:
            return True
        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False
        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#


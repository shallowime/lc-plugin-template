#
# @lc app=leetcode.cn id=701 lang=python3
# @lcpr version=30201
#
# [701] 二叉搜索树中的插入操作
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.insertIntoBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5))



#
# @lcpr case=start
# [4,2,7,1,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [40,20,60,10,30,50,70]\n25\n
# @lcpr case=end

# @lcpr case=start
# [4,2,7,1,3,null,null,null,null,null,null]\n5\n
# @lcpr case=end

#


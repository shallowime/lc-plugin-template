#
# @lc app=leetcode.cn id=538 lang=python3
# @lcpr version=30201
#
# [538] 把二叉搜索树转换为累加树
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
        self.sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
    
    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.convertBST(TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))))



#
# @lcpr case=start
# [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n
# @lcpr case=end

# @lcpr case=start
# [0,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4,1]\n
# @lcpr case=end

#


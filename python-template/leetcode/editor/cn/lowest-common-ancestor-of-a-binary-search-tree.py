#
# @lc app=leetcode.cn id=235 lang=python3
# @lcpr version=30201
#
# [235] 二叉搜索树的最近公共祖先
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if root.val >= p.val and root.val <= q.val:
            return root
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.lowestCommonAncestor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9))), TreeNode(2), TreeNode(8)))



#
# @lcpr case=start
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n8\n
# @lcpr case=end

# @lcpr case=start
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n4\n
# @lcpr case=end

#


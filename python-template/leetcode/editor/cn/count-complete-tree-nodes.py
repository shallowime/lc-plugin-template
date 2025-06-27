#
# @lc app=leetcode.cn id=222 lang=python3
# @lcpr version=30201
#
# [222] 完全二叉树的节点个数
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l = root
        r = root
        hl = 0
        hr = 0
        while l is not None:
            l = l.left
            hl += 1
        while r is not None:
            r = r.right
            hr += 1
        if hl == hr:
            return 2 ** hl - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))



#
# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=654 lang=python3
# @lcpr version=30201
#
# [654] 最大二叉树
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        
        index = -1
        max_val = float('-inf')
        for i in range(left, right + 1):
            if nums[i] > max_val:
                index = i
                max_val = nums[i]

        root = TreeNode(max_val)
        root.left = self.build(nums, left, index - 1)
        root.right = self.build(nums, index + 1, right)
        return root
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.constructMaximumBinaryTree([3,2,1,6,0,5]))


#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#


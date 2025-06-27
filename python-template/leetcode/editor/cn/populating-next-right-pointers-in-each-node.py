#
# @lc app=leetcode.cn id=116 lang=python3
# @lcpr version=30201
#
# [116] 填充每个节点的下一个右侧节点指针
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1, node2):
        if node1 is None or node2 is None:
            return
        node1.next = node2
        self.traverse(node1.left, node1.right)
        self.traverse(node1.right, node2.left)
        self.traverse(node2.left, node2.right)
# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.connect(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))))


#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


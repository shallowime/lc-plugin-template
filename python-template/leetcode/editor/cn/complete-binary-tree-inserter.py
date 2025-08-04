#
# @lc app=leetcode.cn id=919 lang=python3
# @lcpr version=30201
#
# [919] 完全二叉树插入器
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
from queue import Queue
class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.q = Queue()
        self.root = root
        temp = Queue()
        temp.put(root)

        while not temp.empty():
            cur = temp.get()
            if cur.left is not None:
                temp.put(cur.left)
            if cur.right is not None:
                temp.put(cur.right)
            if cur.right is None or cur.left is None:
                self.q.put(cur)

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        cur = self.q.queue[0]
        if cur.left is None:
            cur.left = node
        else:
            cur.right = node
            self.q.get()
        self.q.put(node)
        return cur.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    
    # your test code here




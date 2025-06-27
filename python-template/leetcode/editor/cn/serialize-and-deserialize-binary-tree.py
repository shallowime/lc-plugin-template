#
# @lc app=leetcode.cn id=297 lang=python3
# @lcpr version=30201
#
# [297] 二叉树的序列化与反序列化
#

from collections import deque
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = ','
    NULL = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        sb = []
        self._serialize(root, sb)
        return ''.join(sb)

    def _serialize(self, root, sb):
        if root is None:
            sb.append(self.NULL + self.SEP)
            return
        
        sb.append(str(root.val) + self.SEP)
        self._serialize(root.left, sb)
        self._serialize(root.right, sb)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(self.SEP)
        nodes = deque(nodes)
        return self._deserialize(nodes)
    
    def _deserialize(self, nodes):
        if not nodes:
            return None
        
        first = nodes.popleft()
        if first == self.NULL:
            return None
        root = TreeNode(int(first))
        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))
    print(ans)



#
# @lcpr case=start
# [1,2,3,null,null,4,5]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#


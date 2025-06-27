#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30201
#
# [143] 重排链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stk = []
        p = head
        while p:
            stk.append(p)
            p = p.next

        p = head
        while p:
            lastNode = stk.pop()
            next = p.next
             # 结束条件，链表节点数为奇数或偶数时均适用
            if lastNode == next or lastNode.next == next:
                lastNode.next = None
                break
            p.next = lastNode
            lastNode.next = next
            p = next
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.fromList([1,2,3,4])
    solution.reorderList(head)
    print(head)


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30201
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p = self.find_nth_from_end(dummy, n + 1)
        p.next = p.next.next
        return dummy.next
    
    def find_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        for _ in range(n):
            p1 = p1.next
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.create_head([1, 2, 3, 4, 5])
    res = solution.removeNthFromEnd(head, 2)
    ListNode.print(res)


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#


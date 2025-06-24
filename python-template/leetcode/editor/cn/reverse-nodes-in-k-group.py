#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30201
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        a, b = head, head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        newhead = self.reverseN(a, k)
        a.next = self.reverseKGroup(b, k)
        return newhead

    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pre, cur, nxt = None, head, head.next
        while n > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
            n -= 1
        head.next = cur
        return pre
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.from_list([1, 2, 3, 4, 5])
    print(solution.reverseKGroup(head, 2))



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#


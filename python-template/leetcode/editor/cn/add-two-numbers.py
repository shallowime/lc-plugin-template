#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30201
#
# [2] 两数相加
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        while p1 is not None or p2 is not None or carry > 0:
            val = carry
            if p1 is not None:
                val += p1.val
                p1 = p1.next
            if p2 is not None:
                val += p2.val
                p2 = p2.next
            carry, val = divmod(val, 10)
            p.next = ListNode(val)
            p = p.next
        return dummy.next
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    l1 = ListNode.create_head([2,4,3])
    l2 = ListNode.create_head([5,6,4])
    res = solution.addTwoNumbers(l1, l2)
    ListNode.print(res)


#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#


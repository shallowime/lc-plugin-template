#
# @lc app=leetcode.cn id=876 lang=python3
# @lcpr version=30201
#
# [876] 链表的中间结点
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.create_head([1, 2, 3, 4, 5])
    res = solution.middleNode(head)
    ListNode.print(res)


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=445 lang=python3
# @lcpr version=30201
#
# [445] 两数相加 II
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
        stk1, stk2 = [], []
        while l1 is not None:
            stk1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stk2.append(l2.val)
            l2 = l2.next
        carry = 0
        dummy = ListNode(-1)
        while stk1 or stk2 or carry > 0:
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            carry, val = divmod(val, 10)
            # 构建新节点，直接接在 dummy 后面
            # 需要注意的是，计算结果的高位也应该放在结果链表的左侧，也就是插入到 dummy 节点的后面
            newnode = ListNode(val)
            newnode.next = dummy.next
            dummy.next = newnode
        return dummy.next
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    l1 = ListNode.create_head([7,2,4,3])
    l2 = ListNode.create_head([5,6,4])
    res = solution.addTwoNumbers(l1, l2)
    ListNode.print(res)


#
# @lcpr case=start
# [7,2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30201
#
# [86] 分隔链表
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 存放小于x的链表的虚拟头节点
        dummy1 = ListNode(-1)
        # 存放大于等于x的链表的虚拟头节点
        dummy2 = ListNode(-1)
        # p1，p2指针负责生成结果链表
        p1 = dummy1
        p2 = dummy2
        # p指针负责遍历原链表
        p = head
        while p is not None:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            # 不能直接让p指针前进
            # p = p.next
            # 断开原链表中的每个节点的next指针
            temp = p.next
            p.next = None
            p = temp
        # 连接两个链表
        p1.next = dummy2.next
        return dummy1.next
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.create_head([1, 4, 3, 2, 5, 2])
    res = solution.partition(head, 3)
    ListNode.print(res)


#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#


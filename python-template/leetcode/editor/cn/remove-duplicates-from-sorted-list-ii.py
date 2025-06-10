#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30201
#
# [82] 删除排序链表中的重复元素 II
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        q = head
        while q is not None:
            if q.next is not None and q.next.val == q.val:
                # 跳过重复的节点
                while q.next is not None and q.next.val == q.val:
                    q = q.next
                q = q.next
                # 如果q为空，说明已经遍历到链表的末尾，在p后面接上None
                if q is None:
                    p.next = None
            else:
                p.next = q
                p = p.next
                q = q.next
        return dummy.next
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    head = ListNode.create_head([1, 2, 2])
    res = solution.deleteDuplicates(head)
    ListNode.print(res)


#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=382 lang=python3
# @lcpr version=30201
#
# [382] 链表随机节点
#

import sys
import os
import random

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

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        i = 0
        res = 0
        p = self.head

        while p is not None:
            i += 1
            if 0 == random.randint(0, i - 1):
                res = p.val
            p = p.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

if __name__ == '__main__':
    solution = Solution(ListNode(1, ListNode(2, ListNode(3))))
    # your test code head = [1, 2, 3]
    print(solution.getRandom())
    print(solution.getRandom())
    print(solution.getRandom())




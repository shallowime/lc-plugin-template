#
# @lc app=leetcode.cn id=1019 lang=python3
# @lcpr version=30201
#
# [1019] 链表中的下一个更大节点
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
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        p = head
        while p is not None:
            nums.append(p.val)
            p = p.next
        
        res = [0] * len(nums)
        stk = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stk) > 0 and stk[-1] <= nums[i]:
                stk.pop()
            res[i] = 0 if not stk else stk[-1]
            stk.append(nums[i])
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.nextLargerNodes(ListNode(2, ListNode(1, ListNode(5)))))



#
# @lcpr case=start
# [2,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,4,3,5]\n
# @lcpr case=end

#


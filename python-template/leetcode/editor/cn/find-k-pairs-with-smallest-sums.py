#
# @lc app=leetcode.cn id=373 lang=python3
# @lcpr version=30201
#
# [373] 查找和最小的 K 对数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from queue import PriorityQueue
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 存储三元组 (num1[i], nums2[i], i)
        # i 记录 nums2 元素的索引位置，用于生成下一个节点
        pq = PriorityQueue()
        # 初始化优先级队列，把每一行的第一个元素装进去
        for i in range(len(nums1)):
            pq.put((nums1[i] + nums2[0], nums1[i], nums2[0], 0))

        res = []
        # 执行合并多个有序链表的逻辑
        while not pq.empty() and k > 0:
            _, num1, num2, idx = pq.get()
            k -= 1
            # 链表中的下一个节点加入优先级队列
            next_inx = idx + 1
            if next_inx < len(nums2):
                pq.put((num1 + nums2[next_inx], num1, nums2[next_inx], next_inx))
            
            # 按照数对的元素和升序排序
            pair = [num1, num2]
            res.append(pair)
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    res = solution.kSmallestPairs(nums1, nums2, k)
    print(res)


#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#


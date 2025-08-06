#
# @lc app=leetcode.cn id=433 lang=python3
# @lcpr version=30201
#
# [433] 最小基因变化
#

import sys
import os
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        bank = set(bank)
        q = deque([startGene])

        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == endGene:
                    return step
                
                for i in range(len(cur)):
                    for c in 'ACGT':
                        new_gene = cur[:i] + c + cur[i+1:]
                        if new_gene in bank:
                            q.append(new_gene)
                            bank.remove(new_gene)
            step += 1
        return -1

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))



#
# @lcpr case=start
# "AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AACCGGTT"\n"AAACGGTA"\n["AACCGGTA","AACCGCTA","AAACGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AAAAACCC"\n"AACCCCCC"\n["AAAACCCC","AAACCCCC","AACCCCCC"]\n
# @lcpr case=end

#


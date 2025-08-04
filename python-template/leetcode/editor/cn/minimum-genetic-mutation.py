#
# @lc app=leetcode.cn id=433 lang=python3
# @lcpr version=30201
#
# [433] 最小基因变化
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



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


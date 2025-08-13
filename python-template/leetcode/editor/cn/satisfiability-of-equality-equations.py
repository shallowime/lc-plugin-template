#
# @lc app=leetcode.cn id=990 lang=python3
# @lcpr version=30201
#
# [990] 等式方程的可满足性
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for e in equations:
            if e[1] == '=':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                uf.union(x, y)
        for e in equations:
            if e[1] == '!':
                x = ord(e[0]) - ord('a')
                y = ord(e[3]) - ord('a')
                if uf.connected(x, y):
                    return False
        return True

class UnionFind:
    def __init__(self, n) -> None:
        self.count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def count(self):
        return self.count

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# b"\na"]\n
# @lcpr case=end

# @lcpr case=start
# a"\nb"]\n
# @lcpr case=end

# @lcpr case=start
# b"\nc"\nc"]\n
# @lcpr case=end

# @lcpr case=start
# b"\nc"\na"]\n
# @lcpr case=end

# @lcpr case=start
# c"\nd"\nz"]\n
# @lcpr case=end

#


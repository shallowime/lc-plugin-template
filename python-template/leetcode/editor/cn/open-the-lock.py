#
# @lc app=leetcode.cn id=752 lang=python3
# @lcpr version=30201
#
# [752] 打开转盘锁
#

from collections import deque
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        if '0000' in deads:
            return -1
        
        visited = set()
        q = deque()
        step = 0
        q.append('0000')
        visited.add('0000')

        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == target:
                    return step
                
                for neightbor in self.getNeightbors(cur):
                    if neightbor not in visited and neightbor not in deads:
                        q.append(neightbor)
                        visited.add(neightbor)
            step += 1
        return -1
    
    def getNeightbors(self, cur):
        neighbors = []
        for i in range(4):
            neighbors.append(self.plusOne(cur, i))
            neighbors.append(self.minusOne(cur, i))
        return neighbors
    
    def plusOne(self, cur, i):
        curList = list(cur)
        if curList[i] == '9':
            curList[i] = '0'
        else:
            curList[i] = str(int(curList[i]) + 1)
        return ''.join(curList)
    
    def minusOne(self, cur, i):
        curList = list(cur)
        if curList[i] == '0':
            curList[i] = '9'
        else:
            curList[i] = str(int(curList[i]) - 1)
        return ''.join(curList)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.openLock(["0201","0101","0102","1212","2002"], "0202"))



#
# @lcpr case=start
# ["0201","0101","0102","1212","2002"]\n"0202"\n
# @lcpr case=end

# @lcpr case=start
# ["8888"]\n"0009"\n
# @lcpr case=end

# @lcpr case=start
# ["8887","8889","8878","8898","8788","8988","7888","9888"]\n"8888"\n
# @lcpr case=end

#


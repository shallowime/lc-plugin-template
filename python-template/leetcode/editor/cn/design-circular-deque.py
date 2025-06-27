#
# @lc app=leetcode.cn id=641 lang=python3
# @lcpr version=30201
#
# [641] 设计循环双端队列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.data = [None] * k
        self.first = 0
        self.last = 0
        self.max_cap = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.first = (self.first - 1) % self.max_cap
        self.data[self.first] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
            
        self.data[self.last] = value
        self.last = (self.last + 1) % self.max_cap
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
            
        self.data[self.first] = None
        self.first = (self.first + 1) % self.max_cap
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
            
        self.last = (self.last - 1) % self.max_cap
        self.data[self.last] = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.first]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.last - 1) % self.max_cap]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_cap
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

if __name__ == '__main__':
    obj = MyCircularDeque(3)
    print(obj.insertFront(1))
    print(obj.insertLast(2))
    print(obj.insertFront(3))
    print(obj.insertFront(4))
    print(obj.getFront())
    print(obj.getRear())
    print(obj.isEmpty())




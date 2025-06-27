#
# @lc app=leetcode.cn id=1670 lang=python3
# @lcpr version=30201
#
# [1670] 设计前中后队列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def balance(self):
        if len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if self.size() % 2 == 0:
            self.right.appendleft(val)
        else:
            self.left.append(val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if self.size() == 0:
            return -1
        if self.size() == 1:
            return self.right.popleft()
        e = self.left.popleft()
        self.balance()
        return e

    def popMiddle(self) -> int:
        if self.size() == 0:
            return -1
        if self.size() % 2 == 0:
            e = self.left.pop()
        else:
            e = self.right.popleft()
        self.balance()
        return e

    def popBack(self) -> int:
        if self.size() == 0:
            return -1
        e = self.right.pop()
        self.balance()
        return e

    def size(self) -> int:
        return len(self.left) + len(self.right)


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end

if __name__ == '__main__':
    obj = FrontMiddleBackQueue()
    obj.pushFront(1)
    obj.pushBack(2)
    obj.pushMiddle(3)
    obj.pushMiddle(4)
    print(obj.popFront())
    print(obj.popMiddle())
    print(obj.popMiddle())



#
# @lcpr case=start
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle",\n"popBack", "popFront"]\n[[], [1], [2], [3], [4], [], [], [], [], []]\n
# @lcpr case=end

#


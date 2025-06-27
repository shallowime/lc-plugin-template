#
# @lc app=leetcode.cn id=225 lang=python3
# @lcpr version=30201
#
# [225] 用队列实现栈
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from collections import deque
# @lc code=start
class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_element = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_element = x

    def pop(self) -> int:
        size = len(self.q)
        while size > 2:
            self.q.append(self.q.popleft())
            size -= 1
        self.top_element = self.q[0]
        self.q.append(self.q.popleft())
        return self.q.popleft()
    
    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    print(obj.top())
    print(obj.empty())



#
# @lcpr case=start
# ["MyStack", "push", "push", "top", "pop", "empty"]\n[[], [1], [2], [], [], []]\n
# @lcpr case=end

#


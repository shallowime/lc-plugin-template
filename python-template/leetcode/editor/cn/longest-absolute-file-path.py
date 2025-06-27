#
# @lc app=leetcode.cn id=388 lang=python3
# @lcpr version=30201
#
# [388] 文件的最长绝对路径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stk = []
        max_length = 0
        for part in input.split('\n'):
            depth = part.count('\t')
            while len(stk) > depth:
                stk.pop()
            stk.append(len(part) - depth)
            if '.' in part:
                total_length = sum(stk) + len(stk) - 1
                max_length = max(max_length, total_length)
        return max_length
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print(solution.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
    print(solution.lengthLongestPath("a"))
    print(solution.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt"))


#
# @lcpr case=start
# "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"\n
# @lcpr case=end

# @lcpr case=start
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

# @lcpr case=start
# "file1.txt\nfile2.txt\nlongfile.txt"\n
# @lcpr case=end

#


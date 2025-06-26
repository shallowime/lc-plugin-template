#
# @lc app=leetcode.cn id=395 lang=python3
# @lcpr version=30201
#
# [395] 至少有 K 个重复字符的最长子串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        length = 0
        for i in range(1, 27):
            # 限制窗口中只能有i种不同字符
            length = max(length, self.longestKLetterSubstring(s, k, i))
        return length

    # 寻找 s 中含有 count 种字符，且每种字符出现次数都大于 k 的子串
    def longestKLetterSubstring(self, s: str, k: int, count: int) -> int:
        res = 0
        # 快慢指针维护滑动窗口，左闭右开区间
        left, right = 0, 0
        # 题目说 s 中只有小写字母，所以用大小 26 的数组记录窗口中字符出现的次数
        windowCharCount = [0] * 26
        # 记录窗口中存在几种不同的字符（字符种类）
        windowUniqueCharCount = 0
        # 记录窗口中有几种字符的出现次数达标（大于等于 k）
        windowValidCharCount = 0

        while right < len(s):
            c = s[right]
            if windowCharCount[ord(c) - ord('a')] == 0:
                # 窗口中新增了一种字符
                windowUniqueCharCount += 1
            windowCharCount[ord(c) - ord('a')] += 1
            if windowCharCount[ord(c) - ord('a')] == k:
                # 窗口中新增了一种达标的字符
                windowValidCharCount += 1
            right += 1
            # 当窗口中字符种类大于 count 时，缩小窗口
            while windowUniqueCharCount > count:
                # 移出字符，缩小窗口
                d = s[left]
                if windowCharCount[ord(d) - ord('a')] == k:
                    # 窗口中移出了一种达标的字符
                    windowValidCharCount -= 1
                windowCharCount[ord(d) - ord('a')] -= 1
                if windowCharCount[ord(d) - ord('a')] == 0:
                    # 窗口中移出了一种字符
                    windowUniqueCharCount -= 1
                left += 1
            # 当窗口中字符种类为 count 且每个字符出现次数都满足 k 时，更新答案
            if windowValidCharCount == count:
                res = max(res, right - left)
        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.longestSubstring("aaabb", 3))
    print(solution.longestSubstring("ababbc", 2))


#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#


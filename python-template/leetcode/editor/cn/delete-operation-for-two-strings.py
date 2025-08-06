#
# @lc app=leetcode.cn id=583 lang=python3
# @lcpr version=30201
#
# [583] 两个字符串的删除操作
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        lcs = self.longestCommonSubsequence(word1, word2)
        return m + n - 2 * lcs
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.minDistance("sea", "eat"))
    print(solution.minDistance("leetcode", "etco"))


#
# @lcpr case=start
# "sea"\n"eat"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"etco"\n
# @lcpr case=end

#


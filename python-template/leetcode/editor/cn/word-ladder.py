#
# @lc app=leetcode.cn id=127 lang=python3
# @lcpr version=30201
#
# [127] 单词接龙
#

import sys
import os
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        q = deque([beginWord])
        visited = set([beginWord])
        step = 1

        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                chars = list(cur)
                for i in range(len(chars)):
                    original_char = chars[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == original_char:
                            continue
                        chars[i] = c
                        new_word = ''.join(chars)
                        if new_word in word_set and new_word not in visited:
                            if new_word == endWord:
                                return step + 1
                            q.append(new_word)
                            visited.add(new_word)
                    chars[i] = original_char
            step += 1
        return 0

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))



#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#


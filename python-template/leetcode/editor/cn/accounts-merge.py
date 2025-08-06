#
# @lc app=leetcode.cn id=721 lang=python3
# @lcpr version=30201
#
# [721] 账户合并
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
from collections import deque

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailtoIndex = {}
        for i in range(len(accounts)):
            account = accounts[i]
            for j in range(1, len(account)):
                email = account[j]
                indexes = emailtoIndex.get(email, [])
                indexes.append(i)
                emailtoIndex[email] = indexes

        res = []
        visited_email = set()

        for email in emailtoIndex.keys():
            if email in visited_email:
                continue
            merged_email = []
            q = deque()
            q.append(email)
            visited_email.add(email)

            while q:
                cur_email = q.popleft()
                merged_email.append(cur_email)
                indexes = emailtoIndex[cur_email]
                for index in indexes:
                    account = accounts[index]
                    for j in range(1, len(account)):
                        next_email = account[j]
                        if next_email not in visited_email:
                            q.append(next_email)
                            visited_email.add(next_email)
            user_name = accounts[emailtoIndex[email][0]][0]
            merged_email.sort()
            merged_email.insert(0, user_name)
            res.append(merged_email)
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John",\n"johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]\n
# @lcpr case=end

# @lcpr case=start
# \n[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]\n
# @lcpr case=end

#


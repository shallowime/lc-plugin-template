#
# @lc app=leetcode.cn id=853 lang=python3
# @lcpr version=30201
#
# [853] 车队
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 组合位置和速度，按位置降序排序
        cars = sorted(zip(position, speed), reverse=True)
        
        # 用于存储每个车队到达终点的时间
        times = []
        
        for pos, spd in cars:
            # 计算到达终点所需时间
            time = (target - pos) / spd
            
            # 如果当前车无法追上前车（时间更长），形成新车队
            if not times or time > times[-1]:
                times.append(time)
            
        # 返回车队数量
        return len(times)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 12\n[10,8,0,5,3]\n[2,4,1,1,3]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3]\n[3]\n
# @lcpr case=end

# @lcpr case=start
# 100\n[0,2,4]\n[4,2,1]\n
# @lcpr case=end

#


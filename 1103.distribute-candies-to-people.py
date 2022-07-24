#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
from math import floor
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        dist = [0 for i in range(num_people)]
        cut = 0
        while candies > 0:
            dist[cut % num_people] += min(cut + 1, candies)
            candies -= cut + 1
            cut += 1
        return dist
# @lc code=end
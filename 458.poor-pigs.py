#
# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#

# @lc code=start
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        mat_len = minutesToTest // minutesToDie + 1
        pigs = 1
        while mat_len ** pigs < buckets:
            pigs += 1
        return pigs
# @lc code=end
#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return False if n % 4 == 0 else True
# @lc code=end


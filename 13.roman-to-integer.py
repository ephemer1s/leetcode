#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        return 1000 * s.count('M') + 500 * s.count('D') + 100 * s.count('C') + 50 * s.count('L') + 10 * s.count('X') + 5 * s.count('V') + s.count('I') - 2 * (s.count('IV') + s.count('IX')) - 20 * (s.count('XL') + s.count('XC')) - 200 * (s.count('CD') + s.count('CM'))
# @lc code=end


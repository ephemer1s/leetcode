#
# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#

# @lc code=start
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        '''
        some specific k should be skipped when there goes multiple 5 in single step.
        mod 156 mod 31 mod 6 == 5
        mod 156 mod 31 == 30
        mod 156 == 155
        '''
        levels = [6, 31, 156, 781, 3906, 19531, 97656, 488281, 2441406,
                  12207031, 61035156, 305175781, 1525878906]
        for i in levels[::-1]:
            k = k % i
            if k == i - 1:
                return 0
        return 5
# @lc code=end


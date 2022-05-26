#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # list all factors < sqrt n
        factors = []
        for i in range(1, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)
        factors = list(set((factors)))
        factors.sort()
        if k > len(factors):
            return -1
        else:
            return factors[k - 1]

# @lc code=end


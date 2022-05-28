#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        m, mask = 0, 0

        for i in range(32)[::-1]:
            # print(i)
            mask |= 1 << i
            # print(bin(mask))
            prefixes = {n & mask for n in nums}
            # print([bin(j) for j in prefixes])
            tmp = m | (1 << i)
            # print(bin(m), bin(tmp))
            if any(prefix ^ tmp in prefixes for prefix in prefixes):
                m = tmp

        return m
        
# @lc code=end


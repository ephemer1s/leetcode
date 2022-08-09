#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        n, p, z = [], [], []
        for i in nums:
            if i > 0:
                p.append(i)
            elif i == 0:
                z.append(i)
            else:
                n.append(i)
        N, P = set(n), set(p)
        if z:
            for i in N:
                if -i in P:
                    output.add(tuple((i, 0, -i)))
        if len(z) >= 3:
            output.add(tuple((0, 0, 0)))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                if -(n[i] + n[j]) in P:
                    output.add(tuple(sorted([n[j], n[i], -(n[i] + n[j])])))
        
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if -(p[i] + p[j]) in N:
                    output.add(tuple(sorted([-(p[i] + p[j]), p[i], p[j]])))
        
        return output
                    
# @lc code=end


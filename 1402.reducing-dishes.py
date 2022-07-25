#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#

# @lc code=start

import bisect 

class Solution:
    def calcScore(self, l):
        score = 0
        for i, dish in enumerate(l):
            score += (i + 1) * dish
        return score
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        pos = []
        neg = []
        for i in satisfaction:
            if i >= 0:
                bisect.insort(pos, i)
            else:
                bisect.insort(neg, i)
        bestscore = self.calcScore(pos)
        for i in neg[::-1]:
            pos.insert(0, i)
            score = self.calcScore(pos)
            if score >= bestscore:
                bestscore = score
            else:
                break
        return bestscore
        
# @lc code=end


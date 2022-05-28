#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        v_min = 1
        v_max = max(piles)
        while v_min <= v_max:
            cur_v = (v_min + v_max) // 2
            hours = [math.ceil(i / cur_v) for i in piles]
            cur_h = sum(hours)
            print(v_min, cur_v, v_max, hours)
            if cur_h > h:
                v_min = cur_v + 1
            else:
                v_max = cur_v - 1
        return v_min
        
# @lc code=end


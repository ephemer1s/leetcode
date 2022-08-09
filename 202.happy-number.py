#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.nums = []
    def isHappy(self, n: int) -> bool:
        if n not in self.nums:
            self.nums.append(n)
            sqsum = sum(int(i) ** 2 for i in str(n))
            if sqsum == 1:
                return True
            else:
                return self.isHappy(sqsum)
        else:
            return False
        
# @lc code=end


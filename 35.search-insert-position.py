#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        lp = 0
        rp = len(nums)

        while 1:
            # move pivot
            mid = (lp + rp) // 2
            # print('lp', lp, 'mid', mid, 'rp', rp)

            if lp == rp:
                return lp
            else:
                if nums[mid] >= target:
                    rp = mid
                elif nums[mid] < target:
                    lp = mid + 1
                    

# @lc code=end


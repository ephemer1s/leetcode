#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        p, q = 0, len(numbers) - 1
        while p < q:
            if numbers[p] + numbers[q] < target:
                p += 1
            elif numbers[p] + numbers[q] > target:
                q -= 1
            else:
                return [p + 1, q + 1]
            
# @lc code=end


#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # create 1d array
        nums = []
        for i in matrix:
            nums += i
        if len(nums) == 1:
            return True if nums[0] == target else False
        # apply binsearch
        l, r, pi = 0, len(nums) - 1, len(nums) // 2
        while l <= r:
            print(l, pi, r)
            if nums[pi] == target:
                return True
            elif nums[pi] > target:
                r = pi - 1
            elif nums[pi] < target:
                l = pi + 1
            pi = (l + r) // 2
        return False

# @lc code=end

        '''
        we could do search by lines, that will cost O(m * n) in time.
        as the matrix is strictly sorted 
        we could reshape it to a 1D array and apply binary search
        that will cost O(log(m * n)) of time
        if applying binary search separately on rows and cols
        the cost will be O(logm) for rows and O(logn) for cols.
        which is exactly the same.
        '''
/*
 * @lc app=leetcode id=326 lang=cpp
 *
 * [326] Power of Three
 */

// @lc code=start
class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n == 0) return false;
        else if (n == 1) return true;
        else if (n % 3 != 0) {
            return false;
        }
        else {
            return isPowerOfThree(n / 3);
        }
    }
};
// @lc code=end


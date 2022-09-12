/*
 * @lc app=leetcode id=231 lang=cpp
 *
 * [231] Power of Two
 */

// @lc code=start
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n == 0) return false;
        else if (n == 1) return true;
        else if (n % 2 == 1) {
            return false;
        }
        else {
            return isPowerOfTwo(n / 2);
        }
    }
};
// @lc code=end


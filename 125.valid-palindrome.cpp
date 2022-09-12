/*
 * @lc app=leetcode id=125 lang=cpp
 *
 * [125] Valid Palindrome
 */

// @lc code=start
#include <iostream>
using namespace std;
    
class Solution {
    private:
    char lowerCase(char x){
        if(x >= 'a' && x <= 'z'){
            return x;
        }
        else{
            char b = x - 'A' + 'a';
            return b;
        }
    }
    bool isValid(char ch){
        if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9')){
            return true;
            
        }
        else
            return false;
    }
    public:
    bool isPalindrome(string s) {
        string cleaned = "";
        for (int i = 0; i < s.length(); i++){
            if (isValid(s[i])){
                cleaned.push_back(lowerCase(s[i]));
            }
        }
        int l = 0, r = cleaned.length() - 1;
        while (l < r) {
            // cout << cleaned[l] << cleaned[r] << endl;
            if (cleaned[l] == cleaned[r]) {
                l++;
                r--;
                continue;
            }
            else {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end


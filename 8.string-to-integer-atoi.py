#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def charIsLetter(self, ch):
        if self.charIsFlag(ch) or self.charIsNumber(ch):
            return False
        else:
            return True
    def charIsFlag(self, ch):
        if ch == '+':
            return 1
        elif ch == '-':
            return -1
        else:
            return 0 
    def charIsNumber(self, ch):
        if '0' <= ch <= '9':
            return True
        else:
            return False
        
    def myAtoi(self, s: str) -> int:
        i = 0
        flag = 1
        head = 0
        num = 0
        while i < len(s) and s[i] == ' ':
            # ignore whitespace
            i += 1
        # check sign
        if i < len(s) and not self.charIsNumber(s[i]):
            flag = self.charIsFlag(s[i])
            i += 1
        head = i
        while i < len(s) and self.charIsNumber(s[i]):
            i += 1
        print(flag,head,i)
        if i > 0 and head != i and self.charIsNumber(s[head]):
            num = s[head:i]
        print(num)
        num = flag * int(num)
        if num < -2147483648:
            num = -2147483648
        elif num > 2147483647:
            num = 2147483647
        return num
        
# @lc code=end


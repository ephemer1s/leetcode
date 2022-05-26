#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        parStack = []
        relation = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for i in s:
            if i == '(' or i == '[' or i == '{':
                parStack.append(i)
            elif len(parStack) > 0 and relation[i] == parStack[-1] :
                r = parStack.pop(-1)
            else: 
                return False
        if len(parStack) == 0:
            return True
# @lc code=end


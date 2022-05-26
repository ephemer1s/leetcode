#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pstack = []
        maxlen = 0
        for i in enumerate(s):
            idx, par = i[0], i[1]
            if par == ')':
                ptr = idx
                pstack = [')']
                # print(ptr, pstack)
                curlen = 0 
                tmplen = 0
                while 1:
                    
                    ptr -= 1
                    
                    if ptr == -1:
                        break

                    elif s[ptr] == ')':
                        pstack.append(')')
                    elif s[ptr] == '(':
                        if len(pstack) == 0:
                            break
                        elif len(pstack) > 0:
                            pstack.pop(-1)
                            tmplen += 2
                    # print(ptr, pstack)
                    if len(pstack) == 0 :
                        curlen += tmplen
                        tmplen = 0
                        maxlen = max(maxlen, curlen)

        return maxlen
# @lc code=end


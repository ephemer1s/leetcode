#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
#     def revert(self, s:str):
#         return ''.join([s[len(s) - 1 - i] for i in range(len(s))])
            
#     def longestPalindrome(self, s: str) -> str:
#         p1, p2 = 0, 1
#         lps = s[0]
#         for p2 in range(1, len(s) + 1):
#             for p1 in range(0, p2):
#                 sub = str(s[p1: p2])
#                 # print(sub, self.revert(sub))
#                 if str(self.revert(sub)) == sub:
#                     if len(sub) > len(lps):
#                         lps = sub
#         return lps

    def longestEvenPalindrome(self, s: str) -> str:
        maxlen = 0
        lps = [0, 0]
        for i in range(0, len(s)):
            for j in range(min(i + 1, len(s) - i)):
                if s[i + j] == s[i - j]:
                    if 1 + 2 * j > maxlen:
                        maxlen = 1 + 2 * j
                        lps = [i - j, i + j]
                else:
                    break
        return ''.join(s[lps[0] : lps[1] + 1])
    
    
    def longestOddPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return ''
        else:
            maxlen = 0
            lps = [0, 0]
            for i in range(0, len(s) - 1):
                for j in range(min(i + 1, len(s) - i - 1)):
                    if s[i + j + 1] == s[i - j]:
                        if 1 + 2 * j > maxlen:
                            maxlen = 1 + 2 * j
                            lps = [i - j, i + j + 1]
                    else:
                        break
            return ''.join(s[lps[0] : lps[1] + 1]) if lps[1] != 0 else ''
        
    def longestPalindrome(self, s: str) -> str:
        even = self.longestEvenPalindrome(s)
        odd = self.longestOddPalindrome(s)
        
        return even if len(even) > len(odd) else odd
        
# @lc code=end


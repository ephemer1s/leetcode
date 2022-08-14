#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.chara = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        if len(digits):
            for i in self.chara[digits[0]]:
                if len(digits) > 1:
                    for j in self.chara[digits[1]]:
                        if len(digits) > 2:
                            for k in self.chara[digits[2]]:
                                if len(digits) > 3:
                                    for l in self.chara[digits[3]]:
                                        ret.append(i + j + k + l)
                                else:
                                    ret.append(i + j + k)
                        else:
                            ret.append(i + j)
                else:
                    ret.append(i)
        return ret
                    
# @lc code=end


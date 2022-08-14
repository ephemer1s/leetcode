#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.pars = {
            1: set(['()'])
        }
    def generateParenthesis(self, n: int) -> List[str]:
        if n in self.pars:
            return self.pars[n]
        else:
            # 1. memorized recursive retrieve last pars
            curset = self.generateParenthesis(n - 1)
            # 2. add new pairs: (old) / ()old / old()
            newset = set()
            for i in curset:
                newset.add('(' + i + ')')
                for j in range(len(i)):
                    newset.add(i[:j] + '()' + i[j:])
            self.pars[n] = newset
            return newset
# @lc code=end


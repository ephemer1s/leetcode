#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        dp = []
        path = path.split('/')
        # path = ['/' + i for i in path.split['/']]
        for i in path:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if dp != []:
                    dp.pop()
            else:
                dp.append('/' + i)
        ret = ''
        if dp == []:
            return '/'
        for i in dp:
            ret += i
        return ret
# @lc code=end


#
# @lc app=leetcode id=2273 lang=python3
#
# [2273] Find Resultant Array After Removing Anagrams
#

# @lc code=start
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words
        t = []
        for i in words:
            d = dict()
            for j in i:
                if j not in d:
                    d[j] = 1
                else:
                    d[j] += 1
            t.append((i,d))
        i = 0
        while i < len(t) - 1:
            if t[i][1] == t[i + 1][1]:
                t.pop(i + 1)
            else:
                i += 1
        return [i[0] for i in t]
        
# @lc code=end


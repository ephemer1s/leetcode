#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strlen = min([len(i) for i in strs])
        prefix = ''
        for i in range(strlen):
            chars = list(set([s[i] for s in strs]))
            if len(chars) == 1:
                prefix += chars[0]
            else:
                return prefix
        return prefix

# @lc code=end


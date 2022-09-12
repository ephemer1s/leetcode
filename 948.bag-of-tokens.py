#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        cur = 0
        last = 0
        tokens.sort()
        while tokens:
            if power >= tokens[0]:
                power -= tokens[0]
                cur += 1
                last = cur
                tokens.pop(0)
            elif cur > 0:
                power += tokens[-1]
                cur -= 1
                tokens.pop(-1)
            else:
                return 0
        return last
# @lc code=end


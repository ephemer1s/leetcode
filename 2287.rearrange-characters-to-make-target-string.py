#
# @lc app=leetcode id=2287 lang=python3
#
# [2287] Rearrange Characters to Make Target String
#

# @lc code=start

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        tar = dict()
        for i in target:
            if i not in tar:
                tar[i] = 1
            else:
                tar[i] += 1
        cnt = dict()
        for i in tar.keys():
            cnt[i] = s.count(i) / tar[i]
        print(tar, cnt)
        return int(min([i[1] for i in cnt.items()]))
            
# @lc code=end
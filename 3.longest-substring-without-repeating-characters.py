#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def __init__(self):
        self.dict = {}
        self.max_len = 0
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        # self.dict[s[0]] = 0
        for tail in range(len(s)):
            print(head, tail)
            # if s[tail] in self.dict:
                # self.max_len = max(self.max_len, tail - head + 1)
                # head = self.dict[s[tail]]+1
                # self.dict = {}  # can't reset self.dict here, could lead to other key disappear
            while s[tail] in self.dict:
                self.dict.pop(s[head])
                head += 1
            self.max_len = max(self.max_len, tail - head + 1)
            self.dict[s[tail]] = tail

        return self.max_len
# @lc code=end


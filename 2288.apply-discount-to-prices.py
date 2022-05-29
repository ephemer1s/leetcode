#
# @lc app=leetcode id=2288 lang=python3
#
# [2288] Apply Discount to Prices
#

# @lc code=start

class Solution:
    def getWords(self, s):
        return s.split(' ')
    
    def assembleStr(self, l):
        return ' '.join(l)
        
    def isValid(self, word):
        if word[0] != '$':
            return False
        try:
            float(word[1:])
            return True
        except ValueError:
            return False
        
    def discount(self, price, disc):
        return '$' + '{:0.2f}'.format(float(price[1:]) * (100 - disc) / 100)
        
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = self.getWords(sentence)
        disc = []
        for i in words:
            if self.isValid(i):
                disc.append(self.discount(i, discount)) 
            else:
                disc.append(i)
                
        ans = self.assembleStr(disc)
        return ans

# @lc code=end
#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
class Solution:
    '''
    This is a not-so-good solution, 
    it only used dp, but not bit-manipulation.
    '''
    def validUtf8(self, data: List[int]) -> bool:
        print([format(i, '08b') for i in data])
        while data:
            byte = format(data[0], '08b')
            if byte[0] == '0':
                data.pop(0)
            elif byte[:2] == '10':
                return False
            else:
                dp = [int(i) for i in byte[1:]]
                length = 0
                data.pop(0) # pop dp itself
                while dp and data:
                    if not dp[0] and data[:2] != '10':
                        print(dp, format(data[0], '08b'), 'dp end')
                        break
                    elif dp[0] and format(data[0], '08b')[:2] == '10':
                        print(dp, format(data[0], '08b'), 'pop')
                        data.pop(0)
                        dp.pop(0)
                        length += 1
                    else:
                        print(dp, format(data[0], '08b'), 'false')
                        return False
                    if length > 3:
                        return False
                # print(dp, data)
                if dp[0] and not data:
                    print('data empty with dp not end, false')
                    return False
        return True
# @lc code=end


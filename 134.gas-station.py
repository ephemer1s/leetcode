#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        elif len(gas) == 1:
            return 0
        else:
            nodes = [[i, gas[i] - cost[i]] for i in range(len(gas))]
            while True:                # collapse nodes
                while nodes[0][1] + nodes[1][1] < 0 or nodes[0][1] < 0:
                    nodes.insert(0,nodes.pop(-1))
                while nodes[0][1] + nodes[1][1] >= 0 and nodes[0][1] >= 0:
                    nodes[0][1] += nodes[1][1]
                    nodes.pop(1)
                    if len(nodes) <= 1:
                        return nodes[0][0]
# @lc code=end


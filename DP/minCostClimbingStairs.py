# easy
#On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
#Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
#
#Example 1:
#Input: cost = [10, 15, 20]
#Output: 15
#Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

class Solution:
    def minCostClimbingStairsBottomUp(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cheapest = [0 for i in range(len(cost))]
        
        for i in range(2, len(cost)):
            cheapest[i] = min(cheapest[i - 2] + cost[i - 2], cheapest[i-1] + cost[i-1])
        
        return min(cheapest[-2] + cost[-2], cheapest[-1] + cost[-1])
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min cost to reach stair n is min(min_cost(n-1), min_cost(n-2))
        min_cost = [math.inf] * len(cost)
        min_cost[0], min_cost[1] = 0, 0

        for i, c in enumerate(cost):
            if i < 2:
                continue
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])
            print(min_cost)

        return min(min_cost[-1] + cost[-1], min_cost[-2] + cost[-2])
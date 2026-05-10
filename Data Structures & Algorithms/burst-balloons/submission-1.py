class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}
        def rec(balloons: Tuple[int]) -> int:
            # print(balloons)
            if len(balloons) == 1:
                return balloons[0]

            if balloons in memo:
                return memo[balloons]
            # rebuild the tuple for each popped balloon we try??
            # calculate max points without this balloon:
            max_pop = 0
            for i, balloon in enumerate(balloons):
                new_tuple = balloons[:i] + balloons[i+1:]

                # add points we will get from popping this balloon before returning:
                this_pop = balloon * (balloons[i-1] if i > 0 else 1) * (balloons[i+1] if i < len(balloons) - 1 else 1)
                this_pop += rec(new_tuple)
                max_pop = max(max_pop, this_pop)

            memo[balloons] = max_pop
            return max_pop
        
        return rec(tuple(nums))
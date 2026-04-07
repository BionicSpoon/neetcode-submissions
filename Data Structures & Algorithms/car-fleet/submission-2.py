class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position)
        pos_and_speeds = [(position[i], speed[i]) for i in range(len(position))]
        pos_and_speeds.sort(reverse=True)
        # let's get a minimum finish time for each start pos
        # finish_times = {}
        # for i in range(len(position)):
        #     finish_times[position[i]] = max(finish_times.get(position[i], 0), 
        #                                 (target - position[i]) // speed[i])


        # pos_and_speeds has been reversed already. it contains (pos, speed)
        latest_end_above = 0
        for start, speed in pos_and_speeds:
            
            finish = (target - start) / speed
            print(f'{finish=}')
            if finish <= latest_end_above:
                fleets -= 1
            latest_end_above = max(latest_end_above, finish)

            print(latest_end_above, fleets)

        return fleets
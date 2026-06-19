class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # think of each first instance, last instance pair as an interval
        # then you have to merge each overlapping interval
        # and return the resulting lengths

        # ggez

        intervals = {}
        # [letter: (first, last) indices]

        for i in range(len(s)):
            if s[i] not in intervals:
                intervals[s[i]] = [i]
            else:
                if len(intervals[s[i]]) == 1:
                    intervals[s[i]].append(i)
                else:
                    intervals[s[i]][1] = i
        
        print(intervals)
        # intervals are in place. Now, sort by start. When we encounter an end after the next start (cannot be equal),
        # merge the two intervals (pop the first, replace the second's end with max(end of first, end of second))
        intervals = list(intervals.values())
        intervals.sort(key=lambda x: (x[0]))
        i = 0
        while i < len(intervals) - 1:
            if len(intervals[i]) == 1:
                i += 1
                continue
            if len(intervals[i+1]) == 1 and intervals[i][1] > intervals[i+1][0]:
                intervals.pop(i+1)
                continue
            print(i, intervals)
            if intervals[i][1] > intervals[i+1][0]:
                popped = intervals.pop(i)
                intervals[i] = [popped[0], max(intervals[i][1], popped[1])]
                continue
            i += 1
            

        print(intervals)

        return [x[-1] - x[0] + 1 if x[-1] != x[0] else 1 for x in intervals ]
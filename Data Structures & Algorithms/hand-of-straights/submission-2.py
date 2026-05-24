class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # start by sorting -> starting with the min num,
        # count up until you reach groupSize, incrementing by 1 each time
        hand.sort()
        counts = {}
        for n in hand:
            counts[n] = 1 + counts.get(n, 0)

        # now we have mapped numbers -> counts
        # can increment by 1 each time
        # and decrement that count, removing at 0
        # and restart with the lowest card with a count each iteration

        while counts:
            cur_card = next(iter(counts))
            for n in range(cur_card, cur_card + groupSize):
                if n not in counts or counts[n] == 0:
                    return False
                counts[n] -= 1

                if counts[n] == 0:
                    del counts[n]

        return True
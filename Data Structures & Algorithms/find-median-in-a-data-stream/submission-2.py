class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        # binary search to find insertion pos
        if len(self.nums) == 0:
            self.nums.append(num)
            return
        l = 0
        r = len(self.nums) - 1
        insert_pos = -1
        while l <= r:
            mid = (l + r) // 2
            if num == self.nums[mid]:
                insert_pos = mid
                break
            elif num < self.nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        if insert_pos == -1:
            insert_pos = l
        
        # print("before:", self.nums)
        self.nums.insert(insert_pos, num)
        # print(self.nums)


    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        if len(self.nums) == 1:
            return self.nums[0]
        if len(self.nums) % 2 == 0:
            return (self.nums[mid] + self.nums[mid - 1]) / 2
        return self.nums[mid]

        
        
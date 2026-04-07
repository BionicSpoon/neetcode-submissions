class TimeMap:

    def __init__(self):
        print('init() called')
        self.outer = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(f'set({key}, {value}, {timestamp}) called')
        if key not in self.outer:
            self.outer[key] = [(timestamp, value)]
        else:
            print('in else')
            self.outer[key].append((timestamp, value))

        print(self.outer)


    def get(self, key: str, timestamp: int) -> str:
        print(f'get({key}, {timestamp}) called')

        if key not in self.outer:
            return ''
        arr = self.outer[key]
        # too early timestamp
        if timestamp < arr[0][0]:
            return ''
        if timestamp >= arr[-1][0]:
            return arr[-1][1]
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            t, val = arr[mid]
            if t == timestamp:
                return val
            elif timestamp < t:
                r = mid - 1
            else:
                l = mid + 1
        print(arr, l, r)
        return arr[l-1][1] if l <= timestamp else ''


        if last_key <= timestamp:
            return self.outer[key][last_key]
        else:
            return ''

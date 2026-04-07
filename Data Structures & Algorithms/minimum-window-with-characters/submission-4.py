class Solution:
    def check(self, counts, target):
        return all(counts.get(key, 0) >= target[key] for key in target)

    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        res = ""
        count = {}
        target = Counter(t)
        while l < len(s):
            
            if self.check(count, target):
                print(count, target, f'{self.check(count, target)=}')
                if r - l < len(res) or not res:
                    print(f'changing res to {s[l:r]} | {l=}, {r=}')
                    res = s[l:r]
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            elif r < len(s):
                count[s[r]] = 1 + count.get(s[r], 0)
                r += 1
            else:
                count[s[l]] -= 1
                l += 1

        return res





        #     if count == {'Y': 1, 'X': 1, 'A': 1, 'Z': 1}:
        #         print("FOUND GOOD:", r, l, r - l + 1, len(s))
                
        #     while r < len(s) and not self.check(count, target):
        #         count[s[r]] = 1 + count.get(s[r], 0)
        #         r += 1

        #     if count == {'Y': 1, 'X': 1, 'A': 1, 'Z': 1}:
        #         print("FOUND GOOD:", r, l, r - l + 1, len(s))

        #     # print(count, target, f'{self.check(count, target)=}')
        #     while l < len(s) and self.check(count, target):
        #         # if count == {'B': 1, 'A': 1, 'N': 1, 'C': 1}:
        #         #     print("FOUND GOOD:", r, l, r - l + 1, len(s))
        #         if (min(r, len(s)-1)) - l + 1 < len(res) or not res:
        #             res = s[l:r+1]
        #         print(count, target)
        #         count[s[l]] -= 1
        #         if count[s[l]] == 0:
        #             del count[s[l]]
        #         l += 1
        #     print(f'After shifting {l=}:', len(s), count, target, f'{self.check(count, target)=}')

        #     if l >= len(s) or (min(r, len(s)-1)) - l + 1 < len(t):
        #         break
        #     count[s[l]] -= 1
        #     if count[s[l]] == 0:
        #         del count[s[l]]
        #     l += 1

        # return res
        

        # # l = 0
        # # count = {}
        
        # # for r in range(len(s)):
        # #     count[r] = 1 + count.get(r, 1)
        # #     if self.check(count, target):
        # #         while self.check(count, target):
        # #             count[l] -= 1
        # #             if count[l] == 0:
        # #                 del count[l]
        # #             l += 1
            
        # l = 0
        # r = 0
        # res = ""
        # count = {}
        # target = Counter(t)
        # while l < len(s):
        #     if count == {'Y': 1, 'X': 1, 'A': 1, 'Z': 1}:
        #         print("FOUND GOOD:", r, l, r - l + 1, len(s))

        #     while r < len(s) and not self.check(count, target):
        #         count[s[r]] = 1 + count.get(s[r], 0)
        #         r += 1

        #     if count == {'Y': 1, 'X': 1, 'A': 1, 'Z': 1}:
        #         print("FOUND GOOD:", r, l, r - l + 1, len(s))

        #     # print(count, target, f'{self.check(count, target)=}')
        #     while l < len(s) and self.check(count, target):
        #         # if count == {'B': 1, 'A': 1, 'N': 1, 'C': 1}:
        #         #     print("FOUND GOOD:", r, l, r - l + 1, len(s))
        #         if (min(r, len(s)-1)) - l + 1 < len(res) or not res:
        #             res = s[l:r+1]
        #         print(count, target)
        #         count[s[l]] -= 1
        #         if count[s[l]] == 0:
        #             del count[s[l]]
        #         l += 1
        #     print(f'After shifting {l=}:', len(s), count, target, f'{self.check(count, target)=}')

        #     if l >= len(s) or (min(r, len(s)-1)) - l + 1 < len(t):
        #         break
        #     count[s[l]] -= 1
        #     if count[s[l]] == 0:
        #         del count[s[l]]
        #     l += 1

        # return res
                
            
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counter = {}
        max_frequency = 0
        l = 0
        for i, char in enumerate(s):
            print(f'checking {s[l:i+1]}')
            counter[char] = 1 + counter.get(char, 0)
            max_frequency = max(max_frequency, counter[char])
            while (i - l + 1) - max_frequency > k:
                counter[s[l]] -= 1
                l += 1
            
            longest = max(longest, i - l + 1)

        return longest










        longest = 0
        cur_len = 0
        counter = {s[0]: 0}
        most_frequent_char = s[0]
        l = 0
        for i, char in enumerate(s):
            print(char, f'{most_frequent_char=}, {k=}, {cur_len=}')
            if char == most_frequent_char:
                counter[char] += 1
                cur_len += 1
                longest = max(longest, i - l + 1)
                continue
            if k > 0:
                # include this char
                counter[char] = 1 + counter.get(char, 0)
                if counter[char] > counter[most_frequent_char]:
                    most_frequent_char = char
                    k += 1
                k -= 1
                cur_len += 1
            else: # k == 0, so we must remove one non-most freq char
                counter[char] = 1 + counter.get(char, 1)
                while s[l] == most_frequent_char:
                    l += 1
                    cur_len -= 1
                    counter[most_frequent_char] -= 1
                print(counter)
                counter[s[l]] -= 1
                l += 1
                cur_len -= 1
                k += 1

            longest = max(longest, i - l + 1)

        
        # if s[-1] == most_frequent_char:
        #     cur_len += 1
        # longest = max(longest, cur_len)

        return longest
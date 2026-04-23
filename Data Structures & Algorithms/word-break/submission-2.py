class Solution:
    def wordBreak(self, word: str, wordDict: List[str]) -> bool:
        valid = set(wordDict)
        memo = {}

        def dfs(s: str) -> bool:
            if s in valid:
                return True
            if s in memo:
                return memo[s]

            found = False
            for i in range(len(s)):
                if s[:i+1] in valid:
                    if dfs(s[i+1:]):
                        found = True
                        break

            if found:
                memo[s] = True
                return True

            memo[s] = False
            return False


        return dfs(word)
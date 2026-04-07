class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        ids = {}

        for string in strs:
            key = str(sorted(string))
            if key in ids:
                res[ids[key]].append(string)
            else:
                ids[key] = len(res)
                res.append([string])
        return res
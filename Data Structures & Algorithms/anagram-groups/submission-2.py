class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def checkAnagram(s, t):
        #     if len(s) != len(t):
        #         return False
        #     counts = dict()
        #     for i in range(len(s)):
        #         counts[s[i]] = 1 if s[i] not in counts else counts[s[i]] + 1
        #         counts[t[i]] = -1 if t[i] not in counts else counts[t[i]] - 1
        #     return all(v == 0 for v in counts.values())

        out = defaultdict(list)
        for s in strs:
            counts = [0]*26
            for c in s:
                counts[ord(c)-ord('a')] += 1
            out[tuple(counts)].append(s)
        return [val for val in out.values()]

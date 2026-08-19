class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) - 1
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                if s2[l] in freq:
                    freq[s2[l]] -= 1
                l += 1
            if s2[r] in freq:
                freq[s2[r]] += 1
            if all(count == 0 for count in freq.values()):
                return True
        return False
            
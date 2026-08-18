class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_f = 0
        counts = {}
        maxContig = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_f = max(max_f, counts[s[r]])
            if (r - l + 1) - max_f > k:
                counts[s[l]] -= 1
                l += 1
            maxContig = max(maxContig, r - l + 1)
        return maxContig

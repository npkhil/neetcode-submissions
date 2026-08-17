class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 0
        maxLen = 1
        while r < len(s) - 1:
            r += 1
            while s[r] in s[l:r]:
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        unique = set(nums)
        for n in unique:
            if n - 1 not in unique:
                i = 1
                while n + i in unique:
                    i += 1
                if i > maxLen:
                    maxLen = i
        
        return maxLen
            
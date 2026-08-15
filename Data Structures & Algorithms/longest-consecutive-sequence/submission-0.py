class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0

        unique = set(nums)
        for n in unique:
            if n - 1 not in unique:
                sequence = []
                sequence.append(n)
                i = 1
                while n + i in unique:
                    sequence.append(n + i)
                    i += 1
                if len(sequence) > maxLen:
                    maxLen = len(sequence)
        
        return maxLen
            
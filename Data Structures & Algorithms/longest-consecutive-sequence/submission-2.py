class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lens = defaultdict(int)
        maxLen = 0
        for n in nums:
            if lens[n]:
                continue
            newLen = lens[n - 1] + lens[n + 1] + 1
            lens[n] = newLen
            lens[n - lens[n - 1]] = newLen
            lens[n + lens[n + 1]] = newLen
            if newLen > maxLen:
                maxLen = newLen
        return maxLen
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        req = 0
        acc = 0
        for i in range(n+1):
            if i != n:
                acc ^= nums[i]
            req ^= i
        return acc ^ req 
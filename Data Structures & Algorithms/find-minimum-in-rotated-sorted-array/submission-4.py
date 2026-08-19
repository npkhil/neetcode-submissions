class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            c = (l + r) // 2
            if nums[c] <= nums[c-1]:
                return nums[c]
            if nums[c] > nums[r]:
                l = c + 1
            elif nums[c] > nums[l]:
                r = c - 1
            else:
                r = c - 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                return c
            if nums[l] <= nums[c]:
                if nums[c] > target and target >= nums[l]:
                    r = c - 1
                else:
                    l = c + 1
            else:
                if nums[c] < target and target <= nums[r]:
                    l = c + 1
                else:
                    r = c - 1
        return -1
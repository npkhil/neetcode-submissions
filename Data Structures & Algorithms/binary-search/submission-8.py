class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        idx = -1
        while l <= r:
            c = (l + r) // 2
            if target < nums[c]:
                r = c - 1
            elif target > nums[c]:
                l = c + 1
            else:
                idx = c
                l = r + 1
        return idx
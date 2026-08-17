class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = min(heights[l], heights[r]) * (r - l)
        while l < r:
            maxArea = max(min(heights[l], heights[r]) * (r - l), maxArea)
            l, r = (l+1, r) if heights[l] < heights[r] else (l, r-1)
        return maxArea

class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * n
        for i in range(n):
            if i == 0 or i == 1:
                ways[i] = i + 1
            else:
                ways[i] = ways[i - 1] + ways[i - 2]
        return ways[-1]
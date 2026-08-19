class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(k):
            out = 0
            for pile in piles:
                out += math.ceil(pile / k)
            return out

        piles.sort()
        l = 1
        r = piles[-1]
        mink = -1
        while l <= r:
            k = (l + r) // 2
            t = time(k)
            if t <= h: 
                mink = k
                r = k - 1
            elif t > h:
                l = k + 1
        return mink
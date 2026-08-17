class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0] * (n + 1)
        off = 1
        for i in range(1, n+1):
            if off * 2 == i:
                off = i
            out[i] = 1 + out[i - off]
        return out
            

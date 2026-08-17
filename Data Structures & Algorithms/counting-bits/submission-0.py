class Solution:
    def countBits(self, n: int) -> List[int]:
        def bits(n):
            bits = 0
            while n:
                n &= n - 1
                bits += 1
            return bits
        
        out = []
        for i in range(n + 1):
            out.append(bits(i))
        return out

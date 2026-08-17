class Solution:
    def isHappy(self, n: int) -> bool:
        def ssd(n):
            new = 0
            while n > 0:
                new += (n%10)**2
                n //= 10
            return new
        
        n1 = n
        n2 = ssd(n)
        while n2 != 1:
            if n1 == n2:
                return False
            n1 = ssd(n1)
            n2 = ssd(ssd(n2))
        return True
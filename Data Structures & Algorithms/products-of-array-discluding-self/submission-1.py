class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIndices = []
        product = 1
        for i, n in enumerate(nums):
            if n == 0:
                zeroIndices.append(i)
            else:
                product *= n
        
        out = []
        if len(zeroIndices) == 1:
            for i in range(len(nums)):
                out.append(0)
            out[zeroIndices[0]] = product
        elif len(zeroIndices) > 1:
            out = [0]*len(nums)
        else:
            for n in nums:
                out.append(product//n)

        return out
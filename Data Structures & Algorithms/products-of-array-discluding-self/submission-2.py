class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []

        for _ in nums:
            pref.append(1)
            suff.append(1)
        
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        out = []
        for i in range(len(nums)):
            out.append(pref[i]*suff[i])
        # print(pref)
        # print(suff)
        return out


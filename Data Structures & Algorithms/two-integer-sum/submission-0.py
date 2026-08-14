class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in aux:
                return [aux[diff], i]
            aux[nums[i]] = i
        

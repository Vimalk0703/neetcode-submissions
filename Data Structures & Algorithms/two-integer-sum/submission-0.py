class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (nums[i] + nums[j]) == target and i!=j:
        #             return [i,j]
        # return []
        
      prevMap = {}
      for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
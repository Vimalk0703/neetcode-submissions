class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}
        n = len(nums)//3
        res = []
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        
        for j,k in hashMap.items():
            if k > n:
                res.append(j)

        return res
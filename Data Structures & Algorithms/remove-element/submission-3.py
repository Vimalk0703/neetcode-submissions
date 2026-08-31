class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # new = []
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         continue
        #     new.append(nums[i])  
        # # print(new)
        # # for i in range(len(new)):
        # #     nums[i] = new[i]         
        # # return len(new)
        # return new

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
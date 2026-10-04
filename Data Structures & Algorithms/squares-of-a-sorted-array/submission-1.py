class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = [1] * len(nums)
        new_nums_position = len(nums)-1
        l, r = 0, len(nums)-1
        while l <=r:
            if nums[l] ** 2 > nums[r] ** 2:
                new_nums[new_nums_position] = nums[l] ** 2
                new_nums_position -=1
                l +=1
            # else nums[l] ** 2 < nums[r] ** 2:
            #     new_nums[new_nums_position] = nums[r] ** 2
            #     new_nums_position -=1
            #     r -=1
            else:
                new_nums[new_nums_position] = nums[r] ** 2
                new_nums_position -=1
                r -=1
        print(new_nums)
        return new_nums


            


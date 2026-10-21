class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap = set()
        # for i in nums:
        #     if i in hashmap:
        #         return True
        #     hashmap.add(i)
        # return False


        dup = set()
        for n in nums:
            if n in dup:
                return True
            dup.add(n)
        return False

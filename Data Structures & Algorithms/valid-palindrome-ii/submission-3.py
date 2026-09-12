class Solution:
    def validPalindrome(self, s: str) -> bool:
        # l, r = 0, len(s)-1
        # while l < r:
        #     if s[l] != s[r]:
        #         skipL, skipR = s[l+1:r+1], s[l:r]
        #         return (skipL == skipL[::-1] or
        #                 skipR == skipR[::-1])
        #     l+=1
        #     r-=1
        # return True
        def isvalidPalindrome(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return (isvalidPalindrome(l+1,r)or
                        isvalidPalindrome(l,r-1))
            l+=1
            r-=1
        return True
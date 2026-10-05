class Solution:
    def minSwaps(self, s: str) -> int:
        extraClose = 0
        maxClose = 0
        for i in range(len(s)):
            if s[i] == ']':
                extraClose +=1  
            else:
                extraClose -=1
            maxClose = max(extraClose, maxClose)
        return (maxClose + 1)//2
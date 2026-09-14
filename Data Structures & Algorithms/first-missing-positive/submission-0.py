class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        #Make all the -ve values to 0
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
        
        #Mark negative values in the array as visited
        for i in range(len(A)):
            val = abs(A[i])
            if 1 <= val <= len(A):
                if A[val - 1] > 0:
                    A[val - 1] *= -1
                elif A[val - 1] == 0:
                    A[val - 1] = -1 * (len(A) +1)
        
        for i in range(1, len(A)+1):
            if A[i-1] >= 0:
                return i
        return len(A) + 1
class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        completetoEnd = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in completetoEnd:
                if stack and stack[-1] == completetoEnd[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
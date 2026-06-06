class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        countToMap = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in countToMap:
                if stack and stack[-1] == countToMap[c]:
                    stack.pop()
                else:
                    return False

            else: 
                stack.append(c)
        
        return True if not stack else False
                    
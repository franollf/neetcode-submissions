class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []

        pairs = {")": "(", "]" : "[", "}": "{"}


        # Loop through characters in string
        for c in s:
            # Check if we're at the closing characters
            if c in pairs:
                if not stack or pairs[c] != stack[-1]:
                    return False
                
                stack.pop()

            else:
                stack.append(c)

        return not stack



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opp = {
            ")":"(","}":"{","]":"["
            } 
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack and opp[char] == (stack[-1]): 
                    stack.pop()
                else:
                    return False
        return not stack
   

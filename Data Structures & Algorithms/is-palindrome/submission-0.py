class Solution:
    def isPalindrome(self, s: str) -> bool:
        sWord = s.lower()               #change whole string to lowercase
        #initalize two pointers
        left = 0 
        right = len(s) - 1
        while (left < right):
            if not sWord[left].isalnum():
                left += 1 
                continue
            if not sWord[right].isalnum():
                right -= 1 
                continue
            if sWord[left] != sWord[right]:
                return False
            left += 1
            right -= 1
        return True


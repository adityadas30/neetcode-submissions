class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = {} 
        counts2 = {}
        for char in s: 
            counts1[char] = counts1.get(char, 0) + 1
        for char in t:
            counts2[char] = counts2.get(char, 0) + 1 
        print(counts1)
        print(counts2)
        return counts1 == counts2
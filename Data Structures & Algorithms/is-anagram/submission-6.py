from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsS = Counter(s)
        countsT = Counter(t)
        return countsS == countsT
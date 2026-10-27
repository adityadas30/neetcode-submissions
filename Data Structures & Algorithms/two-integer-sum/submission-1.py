class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in seen:
                print(diff,n)
                return [seen[diff], i]
            seen[n] = i 

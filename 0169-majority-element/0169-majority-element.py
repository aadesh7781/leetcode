class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        s=sorted(nums)
        mid=len(s)//2
        return s[mid]
        
        
        
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq={}
        duplicate=False
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in nums:
            if freq[num]>1:
                duplicate = True
        return duplicate
        
        
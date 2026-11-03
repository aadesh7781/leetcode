class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        coun=0
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]>coun:
                coun=freq[num]
                majority=num
        return majority
        
        
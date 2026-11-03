class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq={}
        arr=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]>=2:
                arr.append(num)
        return arr

        
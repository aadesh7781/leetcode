class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count_even=0
        for num in nums:
            count=0
            while num>0:
                num=num//10
                count+=1
            if count%2==0:
                count_even+=1
        return count_even
                
        
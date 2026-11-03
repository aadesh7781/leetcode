class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low=0
        med=0
        high=len(nums)-1
        while med<=high:
            if nums[med]==0:
                nums[low],nums[med]=nums[med],nums[low]
                low+=1
                med+=1
            elif nums[med]==1:
                med+=1
            else:
                nums[med],nums[high]=nums[high],nums[med]
                high-=1
        
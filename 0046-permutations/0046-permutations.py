
class Solution:
    def permute(self, nums):
        result=[]
        current=[]
        used=[False]*len(nums)

        def backtrack():
            if len(current)==len(nums):
                result.append(current.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    current.append(nums[i])
                    used[i]=True

                    backtrack()

                    current.pop()
                    used[i]=False

        backtrack()
        return result
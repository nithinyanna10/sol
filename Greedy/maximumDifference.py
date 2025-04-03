class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        temp = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    temp = max(temp,abs(nums[i]-nums[j]))
        if temp > 0 :
            return temp 
        else :
            return -1
        

        
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left , right =  0,len(nums)-1
        while left < right :
            if abs(nums[left]) == nums[right] and nums[left]< 0:
                return abs(nums[right]) 
            elif nums[right] +  nums[left] < 0:
                left+=1
            else :
                right-=1
        return -1 

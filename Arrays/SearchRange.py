class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        x = []
        y = [-1, -1]

        for i in range(n):
            if target == nums[i]:
                y[0] = i
                break 
        if y[0] == -1:
            return y 
        
        for i in range(n - 1, -1, -1):
            if nums[i] == target:
                y[1] = i  
                break 

        return y

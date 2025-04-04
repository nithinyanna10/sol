class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums=list(set(nums))
        temp = 0 
        if max(nums) < 0 :
            return max(nums)
        else :
            for i in range(len(nums)):
                if nums[i] > 0 :
                    temp+=nums[i]
        return temp 
        
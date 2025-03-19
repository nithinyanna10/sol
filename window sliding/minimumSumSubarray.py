class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        subarray = []
       
        for i in range(l,r+1):
            for j in range(len(nums)-i+1):
                subarray_sum = sum(nums[j:j+i])
                if subarray_sum > 0:
                    subarray.append(subarray_sum)
        if not subarray:
            return -1

        return min(subarray)
        
        
        
    
        
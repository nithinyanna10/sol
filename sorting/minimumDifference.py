class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        subarray = []
        if len(nums) == 1 :
            return 0 
        for i in range(len(nums)-k+1):
            subarray.append(max(nums[i:i + k])-min(nums[i:i + k]))
        return min(subarray)
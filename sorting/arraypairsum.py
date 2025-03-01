class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sub = []
        for i in range(0,len(nums),2):
            sub.append(min(nums[i:i+2]))
        return sum(sub)
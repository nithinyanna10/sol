class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            for j in range(i+indexDifference,len(nums)):
                if abs(nums[j] - nums[i]) >= valueDifference:
                    return [j, i]
        return [-1,-1]

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k or k<=0 :
            return []
        window = sum(nums[:k])/k
        result = [window]
        for i in range(k,len(nums)):
            window += (nums[i]-nums[i-k])/k
            result.append(window)
        return max(result)
        
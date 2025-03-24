class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n  = len(nums)
        window = sum(nums[:2*k+1])
        arr = []
        arr = [-1] * n
        if 2 * k + 1 > n:
            return arr
        arr[k] = window // (2 * k + 1)
        for i in range(k + 1, n - k):
            window = window - nums[i - k - 1] + nums[i + k]
            arr[i]=window//(2*k+1)
        return arr
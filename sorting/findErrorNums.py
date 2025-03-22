class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        original = list(range(1, len(nums) + 1))
        counter = Counter(nums)
        result = [nums for nums,freq in counter.items() if freq > 1]
        arr = list(set(original) - set(nums))
        print(arr)
        return result+arr
        
        
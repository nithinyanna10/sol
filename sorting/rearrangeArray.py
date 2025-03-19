class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        result = []
        for i in range(len(nums)):
            if nums[i]<0:
                even.append(nums[i])
            else :
                odd.append(nums[i])
        print(even)
        print(odd)
        for a, b in zip(odd, even):
            result.append(a)
            result.append(b)
        return result
        
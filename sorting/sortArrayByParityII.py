class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        result = []
        for i in range(len(nums)):
            if nums[i] % 2 ==0:
                even.append(nums[i])
            else :
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        print(even)
        print(odd)
        for a, b in zip(even, odd):
            result.append(a)
            result.append(b)
        return result

        
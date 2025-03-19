class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for num in nums :
            current = max(b,a+num)
            a = b 
            b = current 
        return b

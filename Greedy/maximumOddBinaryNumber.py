class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_1 = 0
        count_0 = 0
        for char in  s:
            if char == '1' :
                count_1 += 1 
            elif char == '0' :
                count_0 += 1 
        return '1' * (count_1-1) + '0' * count_0 + '1'
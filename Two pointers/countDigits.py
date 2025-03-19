class Solution:
    def countDigits(self, num: int) -> int:
        n = []
        count = 0
        n  = [int(digit) for digit in str(num)]
        for i in range(len(n)):
            if num%n[i] == 0:
                count +=1 
        return count
        
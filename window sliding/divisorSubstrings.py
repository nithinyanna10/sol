class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        y = []
        count = 0
        arr = [int(digit) for digit in str(num)]
        for i in range(len(arr)-k+1):
            x = (arr[i:i+k])
            number = int("".join(map(str, x)))
            if number == 0 :
                count += 0
            elif num % number == 0:
                count +=1 
        return count 
       

        
        
        

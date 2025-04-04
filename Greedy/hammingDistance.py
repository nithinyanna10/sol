class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binary1 = bin(x)[2:]  
        binary1 = str(binary1.zfill(32))
        binary2 = bin(y)[2:]  
        binary2 = str(binary2.zfill(32))
        count = 0
        for i in range(len(binary1)):
            if binary1[i] != binary2[i]:
                count+= 1 
        return count 
        
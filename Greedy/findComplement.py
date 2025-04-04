class Solution:
    def findComplement(self, num: int) -> int:
        binary = str(bin(num)[2:])
        a = 0
        for i in range(len(binary)):
            if binary[i] == '0':
                a =  a*10+1
            elif binary[i] == '1' :
                a =  a*10+0
        comp =   int(str(a),2)
        return comp 
        
        
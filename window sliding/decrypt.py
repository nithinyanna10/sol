class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        a = len(code)
        arr= []
        code = code + code
        n = len(code) 
        if k == 0 :
            return [0] * a
        elif k > 0 :
            for i in range(0,n//2):
                arr.append(sum(code[i+1:k+i+1]))
            
        else:
            for i in range(a):
                arr.append(sum(code[i+a+k:i+a]))
            
        return arr
        
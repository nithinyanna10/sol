class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count =  0
        
        for i in range(0,len(s)-2):
            chunk = s[i:i+3]
            if len(set(chunk))== 3:
                count += 1 
        return count 

        
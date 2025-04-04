class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0 :
            return "0"
        rem  = ""
        count  = 0 
        if num < 0 :
            count += 1 
            num = -num
        while num > 0 :
            rem = str(num%7) + rem
            num=num//7
        if count == 1:
            return ('-' + rem)
        else :
            return rem
        
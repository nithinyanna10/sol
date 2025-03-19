class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 :
            return 1 
        elif n == 2 :
            return 2 
        elif n == 3 :
            return 3 
        else :
            a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b

        
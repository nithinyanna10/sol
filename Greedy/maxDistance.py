class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist  = float("-inf")
        temp = 0
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors)):
                if colors[i] != colors[j]:
                    temp = max(temp,abs(i-j))
        return temp


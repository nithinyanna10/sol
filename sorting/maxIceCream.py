class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0 
        a = 0
        for i in range(len(costs)):
            a += costs[i]
            if a <= coins :
                count +=1 
            else :
                break  
        return count
        
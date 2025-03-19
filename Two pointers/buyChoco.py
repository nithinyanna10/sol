class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        print(prices)
        if prices[0] + prices[1] < money:
            return money - (prices[0] + prices[1])
        elif prices[0] + prices[1] == money:
            return 0 
        else :
            return money
       
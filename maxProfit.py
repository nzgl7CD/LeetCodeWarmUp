class Solution:
    def maxProfit(prices: list[int]) -> int:
        if not prices:
            return 0
        min_price= float('inf')
        max_profit = 0
        for i in prices:
            if i< min_price:min_price=i
            elif i- min_price> max_profit:max_profit = i- min_price
        return max_profit

prices = [7, 1, 5, 3, 6, 4]
result = Solution.maxProfit(prices)
print(result)  

        
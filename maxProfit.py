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
    
    def dynamic_max_profit(arr:list[int])->int:
        profit1,profit2=0,0
        for i in arr:
            temp_profit=max(profit1+i,profit2)
            profit1=profit2
            profit2=temp_profit
        return profit2
    

prices = [7, 1, 5, 3, 6, 4]
result = Solution.maxProfit(prices)
print(result)  

        
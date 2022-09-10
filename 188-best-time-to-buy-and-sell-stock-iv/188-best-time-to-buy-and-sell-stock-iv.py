class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        result = 0 
        if len(prices) == 0:
            return 0
        
        best_days_profit = [0 for x in range(len(prices))]
        
        for number_of_purchases in range(k):
            cheapest_stock_purchase = -prices[0]
            highest_profit = 0
            
            for day in range(1,len(prices)):
                possible_purchase_cost = best_days_profit[day] - prices[day]
                if possible_purchase_cost > cheapest_stock_purchase:
                    cheapest_stock_purchase = possible_purchase_cost
                    
                possible_profit = cheapest_stock_purchase + prices[day]
                if possible_profit > highest_profit:
                    highest_profit = possible_profit
                    
                best_days_profit[day] = highest_profit
            
            if result >= highest_profit:
                return result
            else:
                result = highest_profit
        
        return result
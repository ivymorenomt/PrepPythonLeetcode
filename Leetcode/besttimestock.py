
def maxProfit(prices):
    l, r = 0, 1  
    # we want our left pointer to be our minimum
    # left = buy, right = sell
    maxP = 0
    
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r +=1
        
    return maxP

prices = [7,6,4,3,1]
print(maxProfit(prices))
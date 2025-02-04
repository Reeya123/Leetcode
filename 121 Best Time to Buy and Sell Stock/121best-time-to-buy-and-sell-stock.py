class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        minprice = prices[0]
        
        for elem in prices[1:]: # elem is actually the price each day here not the index\
            if elem > minprice:
                maxprofit = max(maxprofit, elem - minprice)
                
            else:
                minprice = elem
                
        return maxprofit
        
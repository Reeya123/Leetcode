class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxbars = 0 
        costs.sort()
        index = 0 
        while index < len(costs) and coins >= costs[index]:
            coins -= costs[index]
            index += 1
            maxbars += 1
            
        return maxbars
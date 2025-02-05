class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        stack = []
        res = [0] * len(temps)
        
        for index, temp in enumerate(temps):
            
            while stack and stack[-1][0] < temp:
                stack_t , stack_i = stack.pop()
                res[stack_i] = (index - stack_i)
                
            stack.append((temp,index))
            
        return res
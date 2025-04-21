class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        light = 0 
        heavy = len(people) - 1
        
        people = sorted(people)
        count = 0 
        
        while light <= heavy:
            if people[light] + people[heavy] <= limit:
                light += 1
                
            heavy -= 1
            count += 1
            
            
        return count 
            
        
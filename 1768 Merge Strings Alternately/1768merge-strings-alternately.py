class Solution(object):
    def mergeAlternately(self, w1, w2):
        p1 , p2 = 0,0
    
        res = []

            
        while p1 < len(w1) and p2< len(w2):
            res.append(w1[p1])
            res.append(w2[p2])
            
            p1 +=1
            p2 +=1
            
        res.append(w1[p1:])
        res.append(w2[p2:])
            
        
        return ("".join(res))
            
            
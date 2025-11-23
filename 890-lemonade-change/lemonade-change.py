from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = defaultdict(int) #key: bill; value: number of bills
        for index in range(len(bills)):
            #3 bills a customer can give

            if bills[index] == 5:
                #simply increase the counter in hashmap
                hashmap[bills[index]] += 1

            elif bills[index] == 10:
                #return a 5 if any 

                if hashmap[5] >0:
                    hashmap[bills[index]] += 1 #accept the 10$
                    hashmap[5] -= 1
                else: return False
            else: #bill = 20 
            #return 10 and 5; return 5,5,5
                if hashmap[10]>0 and hashmap[5]>0:
                    #accept the 20 first 
                    hashmap[bills[index]] += 1
                    hashmap[10] -= 1
                    hashmap[5] -= 1

                elif hashmap[5]>=3:
                    #qaccept the 20 first (unnecessary)
                    
                    hashmap[5] -= 3
                else: return False
        return True


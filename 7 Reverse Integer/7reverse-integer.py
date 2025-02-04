class Solution(object):
    def reverse(self, x):
        isnegative = True if x < 0 else False 
        x = abs(x)
        reversed_num = 0
        while x!=0: 
            lastdigit = x % 10  #123 % 10 = 3
            
            reversed_num = reversed_num * 10 + lastdigit
            x = x // 10 #12 - remove last element
            
        #res = ','.join(reversed_num)
        if isnegative:
            reversed_num = -reversed_num

        if reversed_num < -2**31 or reversed_num > 2**31 -1 :
            return 0
            
        return reversed_num 
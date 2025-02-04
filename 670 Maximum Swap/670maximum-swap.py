class Solution(object):
    def maximumSwap(self, num):
        digit_list = list(str(num))
        print(digit_list) 
        

        hashmap = { int(digit) : index for index, digit in enumerate(digit_list)}
        print(hashmap)
        
        for index, digit in enumerate(digit_list):
            for d in range(9, int(digit), -1):
                if d in hashmap and hashmap[d] > index:
                    #swapp
                    digit_list[index] , digit_list[hashmap[d]] = digit_list[hashmap[d]] , digit_list[index]
                    
                    return int(''.join(digit_list))
        return num    
                
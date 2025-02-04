class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        if len(v1) < len(v2):
            while len(v1) < len(v2):
                v1.append('0')
        if len(v1) > len(v2):
            while len(v1) > len(v2):
                v2.append('0')    
        
        for index in range(len(v1)):
            '''
            check for 3 conditions:
            If version1 < version2, return -1.
            If version1 > version2, return 1.
            Otherwise, return 0.
            
            '''
            if int(v1[index]) < int(v2[index]):
                return -1
            elif int(v1[index]) > int(v2[index]):
                return 1
            
                
        return 0
        
class Solution(object):
    def busyStudent(self, ST, ET, QT):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        counter = 0 
        for index in range(len(ST)):
            if ST[index] <= QT:
                
                if ET[index] >= QT:
                    
                    counter += 1
                    
                
                    
        return counter
            
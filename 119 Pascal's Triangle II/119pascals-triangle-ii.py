class Solution(object):
    def getRow(self, rowIndex):
        res = [[1]]
        
        for index in range(rowIndex ): # iterate for number of rows 
            temp = [0] + res[-1] + [0]
            row = []
            
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res[-1]
        
class Solution(object):
    def generate(self, Rows):
        res =[[1]]
        for elem in range(Rows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            
            for i in range(len(res[-1]) + 1):
                row.append(temp[i] + temp[i+1])
                
            res.append(row)
            
        return res
            
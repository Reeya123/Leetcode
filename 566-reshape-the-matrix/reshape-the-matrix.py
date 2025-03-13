class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        #get the dimensions of original matrix 
        rows = len(mat)
        cols = len(mat[0])

        '''
        ex - 
        Original matrix size = 2 × 2 = 4 elements
        New matrix size = 1 × 4 = 4 elements
        
        '''
        if rows*cols != r*c: # reshaping is not possible 
            return mat #simply return original mat 
        

                
        #create a nrew matrix of size r , c  
        new_matrix = [[0] * c for r_index in range(r)]
        
        row , col = 0 , 0 
        
        #traverse the original mat and populate the new one 

        for r_index in range(rows):
            for c_index in range(cols):
                new_matrix[row][col] = mat[r_index][c_index]
                
                col += 1
                
                #check if its the end of the row?
                if col == c:
                    col = 0 
                    row += 1
        
        
            
        return new_matrix
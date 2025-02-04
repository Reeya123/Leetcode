class Solution(object):
    def generateMatrix(self, n):
        #create a matrix of size n 
        grid = [[0] * n for _ in range(n)] #fill the matrix of size n with 0s
        
        #intialize the pointers
        left = 0 
        right = n-1 
        top = 0
        bottom = n - 1
        val = 1
        while left <= right and top <= bottom:
            #fill vals in the row
            for col in range(left, right + 1):
                grid[top][col] = val
                
                val += 1
            top += 1
            #fill vals in the last col 
            
            for row in range(top , bottom + 1):
                grid[row][right] = val
                val  += 1
            right -= 1
            
            
            if top <= bottom:
            #fill values in the bottom row (reversed)
                for col in range(right , left - 1 , -1):
                    grid[bottom][col] = val
                    val  += 1
                bottom -= 1 #move the bottom up 

            if left <= right:
            #fill values in the first column 
                for row in range(bottom , top - 1, -1):
                    grid[row ][left] = val
                    val  += 1
                left += 1

                
                
            
        
        return grid

            
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #get the no of rows and cols in the matrix 
        grid_rows = len(grid)
        grid_cols = len(grid[0])

        max_area = 0 
        def dfs(r_index, c_index):
            #1 - check if the cell is  in bounds of the grid 
            if (r_index < 0 or 
            r_index >= grid_rows or 
            c_index < 0 or 
            c_index >= grid_cols or 
            grid[r_index][c_index] != 1):
                return 0
            
            else:
                #mark as visited 
                grid[r_index][c_index] = 0 

            #dfs on adj vals 
                
            
            return (1 + dfs( r_index, c_index + 1) + dfs( r_index, c_index - 1) + dfs( r_index  + 1, c_index ) + dfs( r_index - 1, c_index ))       

                

        

        #iterate over all cells in the matrix 
        for r_index in range(grid_rows):
            for c_index in range(grid_cols):
                if grid[r_index][c_index] == 1:
                    max_area = max(max_area, dfs(r_index, c_index))

        return max_area
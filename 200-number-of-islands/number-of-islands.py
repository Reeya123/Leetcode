class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        
        if not grid:
            return []
        
        def dfs(r_index, c_index):
            
            
            
            '''
            check - 
            if r_index < 0 aand >= grid_rows
            if c_index < 0 and >= grid_cols
            if grid[r_index][c_index] != 1:
            return False
            '''
            if r_index < 0 or r_index >= grid_rows or c_index < 0 or c_index >= grid_cols or grid[r_index][c_index] != '1':

                return 
            
            grid[r_index][c_index] = '0'
            
            #explore all the 4 directions to search for teh next island
            '''
            move rght - x + 1, y
            move left - x - 1, y
            
            move up - x, y + 1
            move down - x, y -1
            
            '''
            directions = [[1, 0] ,[-1 , 0], [0, 1], [0, -1]]
            for off_r , off_c in directions:
                hor_adj = off_r + r_index
                ver_adj = off_c + c_index 
                
                dfs(hor_adj, ver_adj)
        
        
        num_island = 0 
        for r_index in range(grid_rows):
            for c_index in range(grid_cols):
                if grid[r_index][c_index] == '1':
                    num_island += 1
                    dfs(r_index, c_index)
        return num_island
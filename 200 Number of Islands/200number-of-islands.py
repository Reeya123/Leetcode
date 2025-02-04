class Solution(object):
    def numIslands(self, grid):
        #edge case:
        if not grid:
            return 0
        
        #check dimenshions
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        visited = set()
        island = 0
        
        
        def bfs(r_index , c_index): 
            
            q = []
            
            visited.add((r_index , c_index))
            q.append((r_index, c_index))
            
            while q:
                row , col =q.pop() #(0, 0)
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                
                for dr , dc in directions: #for each pair [dr, dc] in directions; dr is the change in row inex and dc is change in col index
                    hor_adj = row + dr #row = 1 dr = 0 then hor_adj = 1,
                    vert_adj = col + dc
                    
                    if (hor_adj in range(grid_rows) and vert_adj in range(grid_cols) and grid[hor_adj][vert_adj] == '1' and (hor_adj , vert_adj) not in visited):
                        q.append((hor_adj , vert_adj))
                        visited.add((hor_adj , vert_adj))
            
        
        
        #Iter ate over all the cells in the grid 
        for r_index in range (grid_rows):
            for c_index in range(grid_cols): #r_index = 0 c_index = 0 so grid[0][0] = '1'
                if grid[r_index][c_index] == '1' and (r_index, c_index) not in visited:
                    bfs(r_index , c_index)
                    island += 1
                    
        return island
            
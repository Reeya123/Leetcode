class Solution(object):
    def findMaxFish(self, grid):
        if not grid:
            return 0
    
        #define the dimensions
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        maxfishes = 0 
        visited = set()
        
        #helper function -bfs: visit theneighbouring cells 
        def bfs(r_index , c_index):
            
            #initializ a queue
            q = []
            q.append((r_index , c_index))
            visited.add((r_index, c_index))
            fishcount = grid[r_index][c_index]
                        
            while q:
                #pop from queue
                row , col = q.pop() # row = 0 col =0
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
                
                for dr , dc in directions: #for each pair in directions, dr is the change of index in direction horizontially and vert
                    
                    hor_adj = row + dr #from the current index, we move right and left to check for fishes 
                    ver_adj = col + dc #from the curr index, we move up and down to check for fishes
                    
                    '''
                    - are these new cordinates in bound? 
                    - is the value of new cell > 0 #means its water 
                    -if the new cordinates are already visited or not? 
                    '''
                    if (hor_adj in range(grid_rows) and ver_adj in range(grid_cols) and grid[hor_adj][ver_adj] > 0 and (hor_adj, ver_adj) not in visited):
                        q.append((hor_adj , ver_adj))
                        visited.add((hor_adj , ver_adj))
                        fishcount += grid[hor_adj][ver_adj]  # Accumulate fish count
                    
            return fishcount
        
        #iterate over every cell
        for r_index in range(grid_rows):
            for c_index in range(grid_cols):
                if grid[r_index][c_index] > 0 and (r_index, c_index) not in visited:
                    
                    maxfishes = max(maxfishes , bfs(r_index , c_index))
                    
        return maxfishes
        
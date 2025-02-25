class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
    
        grid_rows = len(heights)
        grid_cols = len(heights[0])
        
        visited_p = set()
        visited_a = set()
        
        qp = deque()
        qa = deque()
        
        # ✅ Add Pacific Ocean border cells
        for index in range(grid_cols):  # Top row
            qp.append((0, index))
            visited_p.add((0, index))
            
        for index in range(grid_rows):  # Left column
            qp.append((index, 0))
            visited_p.add((index, 0))

        # ✅ Add Atlantic Ocean border cells
        for index in range(grid_cols):  # Bottom row
            qa.append((grid_rows - 1, index))
            visited_a.add((grid_rows - 1, index))

        for index in range(grid_rows):  # Right column
            qa.append((index, grid_cols - 1))
            visited_a.add((index, grid_cols - 1))
        
        def bfs(que, visited):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Right, Left, Down, Up
            
            while que:
                dr, dc = que.popleft()
                
                for r_offset, c_offset in directions:
                    hor_adj = dr + r_offset
                    ver_adj = dc + c_offset
                    
                    # ✅ Check boundaries
                    if 0 <= hor_adj < grid_rows and 0 <= ver_adj < grid_cols:
                        # ✅ Only traverse if height is increasing or same
                        if heights[hor_adj][ver_adj] >= heights[dr][dc] and (hor_adj, ver_adj) not in visited:
                            visited.add((hor_adj, ver_adj))
                            que.append((hor_adj, ver_adj))
        
        bfs(qp, visited_p)
        bfs(qa, visited_a)
        
        # ✅ Find common coordinates that can reach both oceans
        return list(visited_p & visited_a)  

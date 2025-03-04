class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list) #each key is mapped to an empty list. 
        courses = prerequisites 
        for course in courses:
            a,b = course 
            g[a].append(b)
            
            
        unvisited = 0 
        visiting = 1 
        visited = 2
        states = [unvisited] * numCourses #track state of each node.

        
        def dfs(node):
            state = states[node] # we want to know the state of the current node
            if state == visited: 
                return True # we know there are no cycles in this path coz we have done a dfs on it before 
            if state == visiting: 
                return False #we came across a node we already saw at the start of this path. cycle detected 
            
            #if its not either of the two, its unvisited. change the state to visiting 
            states[node] = visiting 
            
            for nei in g[node]: #explore neighbours; TC 
            #if not true== if dfs returned false 
                if not dfs(nei): 
                    return False #there was a cycle in the path hence dfs returned false. 
            
            #if the entire path  is explored and no cycles detected, we good to take the course 
            states[node] = visited 
            return True
        for i in range(numCourses):
            #was there a cycle in the path? did dfs return false?
            if states[i]== unvisited and not dfs(i):
                return False
            
        return True


#TC - like any other grph problem - we go over all the nodes in the graph: O (N + E) we also explore all the edges going out of each node. 
#SC - dfs on each node - O(N) from the recursive call stack  also using defaultdict - storing all edges of the graph ,so O(N + E)
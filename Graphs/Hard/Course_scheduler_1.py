class Solution:
    # There must be no cycle between the nodes 
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = [-1] * numCourses
        visited_path = [-1] * numCourses

        # Creating the adj. list 
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        # This dfs function is for cycle detection 
        def dfs_helper(start):
            visited[start] = 1
            visited_path[start] = 1
            for i in adj[start]:
                if(visited[i] == -1):
                    if(dfs_helper(i) == True):
                        return True
                    # When a cycle is detected while traversing
                elif(visited[i] == 1 and visited_path[i] == 1):
                    return True
            visited_path[start] = 0
            return False
            

        for start in range(numCourses):
            if(visited[start] == -1):
                # If a cycle is fromed straight away return False
                if(dfs_helper(start) == True):
                    return False    
        return True

        
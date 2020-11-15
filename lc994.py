#bfs

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        di = [[-1, 0],[1, 0],[0, 1],[0, -1]]
        q = []
        r = len(grid)
        c = len(grid[0])
        vis = [[-1 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append([i,j])
                    vis[i][j] = 0
        
        while q:
            u = q[0]
            q.pop(0)
            for d in di:
                v = [u[0]+d[0], u[1]+d[1]]
                if v[0] < 0 or v[1] < 0 or v[0] == r or v[1] == c: 
                    continue
                if vis[v[0]][v[1]] == -1 and grid[v[0]][v[1]] == 1:
                    q.append(v)
                    vis[v[0]][v[1]] = vis[u[0]][u[1]] + 1
                    grid[v[0]][v[1]] = 2    
        
        no_fresh = True
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    no_fresh = False
        
        if no_fresh == True:
            return max(0, max([max(v) for v in vis]))
        else:
            return -1
            
        
        

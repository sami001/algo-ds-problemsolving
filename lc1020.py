class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(u):
            cnt = 1
            isIsland = True
            q.append(u)
            vis[u[0]][u[1]] = 1
            while q:
                u = q[0]
                q.pop(0)
                for d in di:
                    v = (u[0]+d[0], u[1]+d[1])
                    if v[0] < 0 or v[1] < 0 or v[0] == r or v[1] == c: 
                        isIsland = False
                    elif grid[v[0]][v[1]] == 1 and vis[v[0]][v[1]] == 0:
                        cnt += 1
                        vis[v[0]][v[1]] = 1
                        q.append(v)
            return cnt if isIsland == True else 0    

        di = [[-1, 0],[1, 0],[0, 1],[0, -1]]
        r = len(grid)
        c = len(grid[0])
        q = []
        vis = [[-1 for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                    vis[i][j] = 0

        tot = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    tot += bfs((i,j))        
        return tot

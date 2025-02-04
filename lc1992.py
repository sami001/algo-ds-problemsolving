#dfs

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        r = len(land)
        c = len(land[0])

        vis = [[False for j in range(c)] for i in range(r)]
        group = []

        def dfs(i, j):
            if vis[i][j] == True:
                return
            vis[i][j] = True
            group.append((i, j))
            for (x,y) in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if x >= 0 and y >= 0 and x < r and y < c and land[x][y] == 1:
                    dfs(x, y)
                    
        ans = []
        for i in range(r):
            for j in range(c):
                if land[i][j] == 1:
                    group = []
                    dfs(i, j)
                    if group:
                        min_x = min([g[0] for g in group])
                        min_y = min([g[1] for g in group])
                        max_x = max([g[0] for g in group])
                        max_y = max([g[1] for g in group])
                        ans.append([min_x, min_y, max_x, max_y])
        return ans
        

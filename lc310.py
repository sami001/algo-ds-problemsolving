#tree diameter
#bfs

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        def bfs(u):
            q = []
            vis, dis, parent = [False] * n,  [0] * n, [-1] * n
            
            q.append(u)
            vis[u] = True
            while q:
                u = q[0]
                q.pop(0)
                for v in graph[u]:
                    if vis[v] == False:
                        dis[v] = dis[u] + 1
                        vis[v] = True
                        parent[v] = u
                        q.append(v)
            return dis, parent

        graph = [[] for i in range(n)]
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])


        dist_, parent_ = bfs(0)
        dist, parent = bfs(dist_.index(max(dist_)))

        ans = []
        u = dist.index(max(dist))

        while u != -1:
            ans.append(u)           #backtracking to create path
            u = parent[u]
            
        Q = len(ans)
        return list(set([ans[Q//2], ans[(Q-1)//2]]))

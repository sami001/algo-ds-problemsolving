#https://leetcode.com/problems/smallest-string-with-swaps/submissions/

#unionfind
#disjointset



class Solution:

    

    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
            
        N = len(s)
        
        rank = [1 for i in range(N)]
        parent = [i for i in range(N)]
        
        
        def find(v):
            if parent[v] == v: return v
            return find(parent[v])
    
        def union(u, v):
            u = find(u)
            v = find(v)

            if u == v: return
            if rank[u] > rank[v]: u, v = v, u
            rank[v] += rank[u]
            parent[u] = v

        for p in pairs:
            union(p[0], p[1])
        
        
        dict = {}
        for i in range(N):
            parent[i] = find(i)
            if parent[i] in dict:
                dict[parent[i]].append(s[i])
            else:
                dict[parent[i]] = [s[i]]
        
        for k in dict:
            dict[k].sort()

        ans = ''
        
        for i in range(N):
            ans += dict[parent[i]][0]
            dict[parent[i]].pop(0)
        
        return ans

            
    
    

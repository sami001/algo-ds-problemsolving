#dp
#memoization
#https://leetcode.com/problems/longest-string-chain/

class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        
        ln = len(words)
        
        graph = [[] for i in range(ln)]
        
        def isParent(w1, w2):
            if len(w2) != (len(w1) + 1):
                return False
            for i in range(len(w2)):
                if w1 == w2[:i]+w2[i+1:]:
                    return True
            return False
        
        def dp(node) -> int:
            if mem[node] != -1:
                return mem[node]
            
            if not graph[node]:
                mem[node] = 1
                return mem[node]
            
            for child in graph[node]:
                mem[node] = max(mem[node], dp(child) + 1)
            
            return mem[node]
                

        for i in range(ln):
            for j in range(ln):
                if isParent(words[i], words[j]) == True:
                    graph[i].append(j)
                    
        for i in range(ln):
            print(graph[i])
                    
        mem = [-1 for i in range(ln)]
        
        ans = 0
        for i in range(ln):
            ans = max(ans, dp(i))
            
        return ans

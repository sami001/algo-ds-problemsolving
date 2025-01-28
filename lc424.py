#two pointers

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [[0 for i in range(26)] for j in range(len(s))]
        
        for i in range(len(s)):
            for j in range(26):
                if i > 0:
                    counter[i][j] = counter[i-1][j]
            counter[i][ord(s[i])-ord('A')] += 1 

        p1 = 0 #pointer 1
        p2 = 0 #pointer 2
        maxLen = -1
        maxRep = -1
        while p1 < len(s):
            maxOccur = -1
            for i in range(0, 26):
                maxOccur = max(maxOccur, (counter[p1][i]-counter[p2-1][i]) if p2 > 0 else counter[p1][i])
            if (p1-p2+1) - maxOccur > k:
                p2 += 1
            else:
                maxRep = max(maxRep, p1-p2+1)
                p1 += 1
        return maxRep
            
  

            
        

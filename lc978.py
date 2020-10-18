#twopointers

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        p1 = 0
        p2 = 0
        ln = 0
        ans = 0
        cur = 0
        while (p1 < len(s) and p2 <= p1):
            cost = abs(ord(s[p1]) - ord(t[p1]))
            if(cost + cur <= maxCost):
                cur += cost
                p1 += 1
                ln += 1
            else:
                cost = abs(ord(s[p2]) - ord(t[p2]))
                cur = max(cur-cost, 0)
                p2 += 1
                ln = max(ln-1, 0)
            if p2 > p1:
                p1 += 1
                
            ans = max(ans, ln)
            
        return ans
            
                
                
            
        

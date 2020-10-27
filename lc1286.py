#https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
#binarysearch

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def sum_div(d):
            sm = 0
            for n in nums:
                if n%d == 0:
                    sm += (n/d)
                else:
                    sm += ((n//d)+1)
            return sm    
        
        lo = 1
        hi = max(nums)
        
        ans = None
        while lo <= hi:
            mi = (lo+hi)//2
            if sum_div(mi) <= threshold:
                hi = mi-1
                ans = mi
            else:
                lo = mi+1
        return ans

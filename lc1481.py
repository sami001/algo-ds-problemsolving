#greedy

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt  = Counter()
        
        for n in arr:
            cnt[n] += 1
        
        elem_cnt = []
        for key in cnt:
            elem_cnt.append(cnt[key])
        elem_cnt.sort()
        
        #print(elem_cnt)
        
        for i in range(len(elem_cnt)):
            #print(k)
            temp = elem_cnt[i]
            elem_cnt[i] = max(0, elem_cnt[i]-k)
            k = max(0, k-temp)
            
            if k == 0:
                break
        #print(elem_cnt)
        return len([x for x in elem_cnt if x > 0])
            

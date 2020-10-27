#priorityqueue
#prime

from queue import PriorityQueue

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq = PriorityQueue()
        pq.put(1)

        
        while n > 1:
            
            num = pq.get()
            
            while not pq.empty() and pq.queue[0] == num:
                pq.get()
            
            pq.put(num * 2)
            pq.put(num * 3)
            pq.put(num * 5)
            
            n -= 1
        return pq.get()

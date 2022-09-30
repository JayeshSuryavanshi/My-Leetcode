import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        n = len(buildings)
        
        res = []
        heap = []
        heapq.heappush(heap,0)
        maxval = 0
        
        result = []
        for i in range(n):
            x,y,h = buildings[i]
            result.append([x,h,0])
            result.append([y,h,1])
            
        result.sort(key = lambda x: (x[0],x[1] if x[2] else -x[1])) 
        
        for u,v,w in result:
            if w == 0:
                heapq.heappush(heap,-v)
                if heap[0] != maxval:
                    maxval = heap[0]
                    res.append([u,v])
                    
            else:
                heap.remove(-v)
                heapq.heapify(heap)
                if heap[0] != maxval:
                    maxval = heap[0]
                    res.append([u,-maxval])
        return res

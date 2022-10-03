class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start, end = 0, 1
        result = []
        
        intervals.sort( key = lambda x: (x[start], x[end] ) ) 
        
        for interval in intervals:
            
            if not result or ( result[-1][end] < interval[start] ):
                result.append( interval )
            
            else:
                result[-1][end] = max(result[-1][end], interval[end])
        return result
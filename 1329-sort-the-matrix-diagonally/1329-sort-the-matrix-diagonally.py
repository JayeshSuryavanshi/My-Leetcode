class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        
        for key in d:
            d[key].sort()
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop(0)
        
        return mat
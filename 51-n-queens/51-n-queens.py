class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, col, l_diagonal, r_diagonal = [], set(), set(), set()
		
        def dfs(r, pos): 
			# r: int, current row to set
			# pos: List[int], previous positioned Queens (at each row)
            if r == n:
                res.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in pos])
                return
            for c in range(n):
                if not c in col and not r - c in l_diagonal and not r + c in r_diagonal:
                    col.add(c)
                    l_diagonal.add(r - c)
                    r_diagonal.add(r + c)
                    dfs(r + 1, pos + [c])
                    col.remove(c)
                    l_diagonal.remove(r - c)
                    r_diagonal.remove(r + c)
            
        dfs(0, [])
        return res
        
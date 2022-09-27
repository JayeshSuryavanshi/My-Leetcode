class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        roots, get = [i for i in range(26)], lambda x: ord(x) - ord('a')
        
        def find(x):
            return x if roots[x] == x else find(roots[x])
        
        for a,op,_,b in equations:
            if op == '=':
                roots[find(get(a))] = find(get(b))
        
        for a,op,_,b in equations:
            if op == '!' and find(get(a)) == find(get(b)): return False
        return True

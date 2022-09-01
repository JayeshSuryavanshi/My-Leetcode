class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pairs = {}
        for i in paths:
            pairs[i[0]] = i[1]
			
        for src, dest in paths:
            if dest not in pairs:
                return dest
        
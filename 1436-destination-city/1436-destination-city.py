class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities_1 = []
        cities_2 = []
        
        for path in paths:
            cities_1.append(path[0])
            cities_2.append(path[1])
        for path in cities_2:
            if path not in cities_1: return path
        
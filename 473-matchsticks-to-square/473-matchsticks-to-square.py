class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = len(matchsticks)
        perimeter = sum(matchsticks)
        
        if perimeter % 4 != 0: 
            return False
        target = perimeter // 4
        
        total = (1 << length)-1
        
        @cache
        def check(mask, s):
            if mask == total: 
                return s == 0
            for i in range(length):
                if mask & (1<<i): 
                    continue
                perimeter = s + matchsticks[i]
                if perimeter == target and check(mask | (1<<i), 0):
                    return True
                if perimeter < target and check(mask | (1<<i), perimeter):
                    return True
            return False
        
        return check(0, 0)
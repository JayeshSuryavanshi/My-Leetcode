class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0 :
            return 0
        _list = list(s.strip())
        if len(_list) == 0 : 
            return 0
        sign = -1 if _list[0] == '-' else 1
        
        if _list[0] in ['-','+']: 
            del _list[0]
        ret, i = 0, 0
        while i < len(_list) and _list[i].isdigit() :
            ret = ret*10 + ord(_list[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
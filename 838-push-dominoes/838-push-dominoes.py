class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = "L" + dominoes + "R"

        p, q = 0, 1
        result = ""
        
        while q < len(s):
            if s[q] != ".":
                if s[p] == s[q]:
                    result += s[p] * (q - p )
                    
                elif s[p] == 'R' and s[q] == 'L':
                    m = (p + q) // 2
                    if (p + q) % 2 == 0: 
                        result += s[p] * (m - p)  + '.' +  s[q] * ( q - m - 1)
                    else:
                        result += s[p] * (m - p + 1) + s[q] * (q - m - 1)
                else:
                    result += s[p] + '.' * (q - p - 1)
                
                p = q 
                
            q += 1
        
        return result[1:]
class Solution:
    def myAtoi(self, s: str) -> int:
        s=list(s)
        isNegative = False

        i = 0
        while i<len(s) and s[i]==" ":
            i+=1
        if i<len(s) and s[i] == '-':
            isNegative = True
            i+=1
        elif i<len(s) and s[i] == '+':
            isNegative = False
            i+=1
            
        total = 0
        
        while i<len(s) and s[i].isdigit():
            total = total*10 + int(s[i])
            i+=1
            if not isNegative and total > 2147483647:
                total = 2147483647
                break
            elif isNegative and total > 2147483648:
                total = 2147483648
                break
        
        if isNegative:
            return -total
        else:
            return total
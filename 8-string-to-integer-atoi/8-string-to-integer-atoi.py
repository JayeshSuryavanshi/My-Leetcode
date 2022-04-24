class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        positive = True
        while(i<len(s) and s[i]==" "):
            i+=1
        if i < len(s) and ord(s[i]) == 45 :
            positive = False
            i+=1
        elif i < len(s) and ord(s[i]) == 43:
            i+=1
            
        num = 0
        while i< len(s) and (48<=ord(s[i])<=57):
            num = num*10 + (ord(s[i])-48)
            i+=1
        if not positive:
            if -num < -2147483648:
                return -2147483648
            return -num
        if num>2147483647:
            return 2147483647
        return num
    
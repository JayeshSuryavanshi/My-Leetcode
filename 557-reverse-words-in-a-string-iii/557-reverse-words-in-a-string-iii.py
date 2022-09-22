class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        ser = []
        final = ''
        for word in res:
            ser.append(word[::-1])        
        return ' '.join(ser)
            
            
        
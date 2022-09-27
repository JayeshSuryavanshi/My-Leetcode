class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {}
        # creating a dictionary mapping of letters to numbers 
        for i in range(1,27):
            if i<=9:
                d[str(i)]=chr(96+i)
            else:
                # appending # to our numbers greater than 10
                d[str(i)+'#']=chr(96+i)
                
        return ''.join([d[i] for i in re.findall(r'\d{2}#|\d', s)])
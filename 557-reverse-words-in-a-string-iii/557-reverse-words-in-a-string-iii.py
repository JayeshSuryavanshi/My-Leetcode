class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        temp = []
        final = " "
        def rev(word):
            return word[::-1]
        for w in a:
            temp.append(rev(w))
        return final.join(temp)

            
            
            

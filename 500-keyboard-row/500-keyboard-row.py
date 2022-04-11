class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first, second, third = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        final = []
        
        for word in words:
            if word[0].lower() in first:
                if all(chars in first for chars in word.lower()):
                    final.append(word)
            if word[0].lower() in second:
                if all(chars in second for chars in word.lower()):
                    final.append(word)
            if word[0].lower() in third:
                if all(chars in third for chars in word.lower()):
                    final.append(word)          
        return final
        
        
                
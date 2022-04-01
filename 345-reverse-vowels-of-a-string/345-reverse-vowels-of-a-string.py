class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set('AEIOUaeiou')
        string = list(s)
        
        # POINTERS
        left = 0
        right = len(string) - 1
        
        while left <= right:
            if string[left] in vowels and string[right] in vowels:
                #SWAP IN PLACE
                string[left], string[right] = string[right], string[left]
                
            elif string[right] not in vowels:
                right = right - 1
                continue
     
            elif string[left] not in vowels:
                left = left + 1
                continue
                
            left += 1
            right -= 1
        
        return ''.join(string)
                
            
        
        
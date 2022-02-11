class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = {},{}
        
        for letter in s:
            a[letter] = a.get(letter, 0) + 1
        
        for letter in t:
            b[letter] = b.get(letter, 0) + 1
            
        return a == b
            
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        'Checking using inbuilt string functions'
        return word.isupper() or word.islower() or word.istitle()
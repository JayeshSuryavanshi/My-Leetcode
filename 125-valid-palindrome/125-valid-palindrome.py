class Solution:
    def isPalindrome(self, s: str) -> bool:  
        
        # re.sub(pattern, repl, string)
        # This regex can practically clean any impure string
        new_string = re.sub("[^a-zA-Z0-9]+","",s).lower()
        
        # checking if reversed string is equal to the original string
        return new_string[:] == new_string[::-1]
        
        
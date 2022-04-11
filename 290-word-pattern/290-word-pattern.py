class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ") #to separate each word from the string. 
        print(words)
        hashmap = {}

        
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)): 
            return False 
        for i in range(len(pattern)):
            if pattern[i] not in hashmap: 
                hashmap[pattern[i]] = words[i] 
            elif hashmap[pattern[i]] != words[i]:
                return False 

        return True 
        
        
        
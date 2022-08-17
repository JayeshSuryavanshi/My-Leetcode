class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookup = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                  ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                  "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        def morse(word):
            final = []
            for c in word:
                final.append(lookup[ord(c) - ord('a')])
            return "".join(final)
        
        _set = set()
        for word in words:
            _set.add(morse(word))
        return len(_set)
            
        